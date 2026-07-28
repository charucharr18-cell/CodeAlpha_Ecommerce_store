from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Seeds database with initial sample categories and e-commerce products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database with sample e-commerce data...')

        categories_data = [
            {'name': 'Electronics', 'icon': 'bi-headset', 'description': 'Gadgets, headphones, wearables and smart tech.'},
            {'name': 'Fashion', 'icon': 'bi-bag-heart', 'description': 'Trendy clothing, stylish shoes and premium accessories.'},
            {'name': 'Home & Living', 'icon': 'bi-house-door', 'description': 'Modern home décor, lighting and essentials.'},
            {'name': 'Gaming', 'icon': 'bi-controller', 'description': 'Next-gen consoles, controllers, and gear.'},
        ]

        categories_map = {}
        for cat_info in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_info['name'],
                defaults={'icon': cat_info['icon'], 'description': cat_info['description']}
            )
            categories_map[cat.name] = cat
            if created:
                self.stdout.write(f'Created category: {cat.name}')

        products_data = [
            {
                'name': 'Wireless Noise-Canceling Headphones',
                'category': 'Electronics',
                'description': 'Experience immersive acoustic depth with active noise cancellation, 30-hour battery life, ultra-soft memory foam earcups, and crystal-clear voice microphone.',
                'price': 149.99,
                'original_price': 199.99,
                'stock': 25,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&auto=format&fit=crop&q=80',
            },
            {
                'name': 'Ultra-Slim AMOLED Smartwatch',
                'category': 'Electronics',
                'description': 'Track your fitness, heart rate, sleep quality, and GPS location with precision. Features vibrant edge-to-edge AMOLED display and 7-day battery life.',
                'price': 89.99,
                'original_price': 129.99,
                'stock': 15,
                'rating': 4.6,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&auto=format&fit=crop&q=80',
            },
            {
                'name': 'Ergonomic Wireless Mechanical Keyboard',
                'category': 'Electronics',
                'description': 'Custom tactile mechanical switches with dynamic RGB backlighting, dual Bluetooth/USB-C connection, and long-lasting rechargeable battery.',
                'price': 119.50,
                'original_price': 149.99,
                'stock': 20,
                'rating': 4.7,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&auto=format&fit=crop&q=80',
            },
            {
                'name': 'Classic Minimalist Leather Watch',
                'category': 'Fashion',
                'description': 'Handcrafted genuine leather strap with stainless steel casing, Japanese quartz movement, and 30m water resistance. Timeless elegance for any occasion.',
                'price': 75.00,
                'original_price': 95.00,
                'stock': 12,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=800&auto=format&fit=crop&q=80',
            },
            {
                'name': 'Urban Streetwear Denim Jacket',
                'category': 'Fashion',
                'description': 'Premium heavy-duty denim jacket with fleece lining, brass buttons, and reinforced stitching. Perfect blend of warmth, comfort, and bold streetwear aesthetic.',
                'price': 64.99,
                'original_price': 85.00,
                'stock': 18,
                'rating': 4.5,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=800&auto=format&fit=crop&q=80',
            },
            {
                'name': 'Minimalist Ceramic Desk Lamp',
                'category': 'Home & Living',
                'description': 'Warm ambient LED lighting with adjustable brightness touch sensor, eco-friendly ceramic base, and woven linen lampshade.',
                'price': 45.00,
                'original_price': 60.00,
                'stock': 30,
                'rating': 4.4,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=800&auto=format&fit=crop&q=80',
            },
            {
                'name': 'Next-Gen Wireless Pro Gamepad',
                'category': 'Gaming',
                'description': 'Low-latency wireless gamepad featuring hall-effect drift-free joysticks, customizable rear paddles, haptic feedback rumble, and multi-platform compatibility.',
                'price': 59.99,
                'original_price': 79.99,
                'stock': 40,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?w=800&auto=format&fit=crop&q=80',
            },
            {
                'name': 'Studio Reference 4K Action Camera',
                'category': 'Electronics',
                'description': 'Capture 4K 60fps video with ultra-smooth electronic image stabilization, 10m waterproof body, dual touchscreen displays, and wide-angle lens.',
                'price': 210.00,
                'original_price': 250.00,
                'stock': 8,
                'rating': 4.7,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800&auto=format&fit=crop&q=80',
            },
        ]

        for prod_info in products_data:
            cat = categories_map[prod_info['category']]
            prod, created = Product.objects.get_or_create(
                name=prod_info['name'],
                defaults={
                    'category': cat,
                    'description': prod_info['description'],
                    'price': prod_info['price'],
                    'original_price': prod_info['original_price'],
                    'stock': prod_info['stock'],
                    'rating': prod_info['rating'],
                    'is_featured': prod_info['is_featured'],
                    'image_url': prod_info['image_url'],
                }
            )
            if created:
                self.stdout.write(f'Created product: {prod.name}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded database!'))
