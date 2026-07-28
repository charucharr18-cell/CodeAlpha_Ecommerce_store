import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, Product, Cart, CartItem, Order, OrderItem
from .context_processors import get_or_create_cart

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    selected_category = request.GET.get('category')
    search_query = request.GET.get('q')

    if selected_category:
        products = products.filter(category__slug=selected_category)

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
        'search_query': search_query,
    }
    return render(request, 'store/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'store/product_detail.html', context)

def cart_detail(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('product').all()
    shipping_cost = 0.00 if cart.subtotal > 100 or cart.subtotal == 0 else 10.00
    tax = round(float(cart.subtotal) * 0.08, 2)
    grand_total = float(cart.subtotal) + shipping_cost + tax

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'shipping_cost': shipping_cost,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)

    quantity = int(request.POST.get('quantity', 1))

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json':
        return JsonResponse({
            'success': True,
            'message': f'"{product.name}" added to cart!',
            'cart_count': cart.total_items
        })

    messages.success(request, f'Added {product.name} to your cart.')
    return redirect('store:cart_detail')

def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
            cart_item.save()
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        elif action == 'set':
            new_qty = int(request.POST.get('quantity', 1))
            if new_qty > 0:
                cart_item.quantity = new_qty
                cart_item.save()
            else:
                cart_item.delete()

    return redirect('store:cart_detail')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.info(request, f'Removed {product_name} from your cart.')
    return redirect('store:cart_detail')

def checkout(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()

    if not cart_items:
        messages.warning(request, 'Your cart is empty.')
        return redirect('store:product_list')

    shipping_cost = 0.00 if cart.subtotal > 100 else 10.00
    tax = round(float(cart.subtotal) * 0.08, 2)
    grand_total = float(cart.subtotal) + shipping_cost + tax

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            zip_code=zip_code,
            total_price=grand_total,
            status='Processing'
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
            # Reduce stock
            item.product.stock = max(0, item.product.stock - item.quantity)
            item.product.save()

        # Clear cart
        cart_items.delete()

        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('store:order_success', order_id=order.id)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'shipping_cost': shipping_cost,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/checkout.html', context)

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'store/order_success.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_history.html', {'orders': orders})
