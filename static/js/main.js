// Main interactive scripts for CodeAlpha E-Commerce Store

document.addEventListener('DOMContentLoaded', () => {
    // Quick Add to Cart via AJAX/Fetch API
    const addToCartForms = document.querySelectorAll('.ajax-add-to-cart');

    addToCartForms.forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const actionUrl = form.action;
            const formData = new FormData(form);

            try {
                const response = await fetch(actionUrl, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                });

                if (response.ok) {
                    const data = await response.json();
                    if (data.success) {
                        // Update Navbar Cart Badge
                        const badge = document.querySelector('.cart-badge');
                        if (badge) {
                            badge.textContent = data.cart_count;
                            badge.classList.add('pulse');
                            setTimeout(() => badge.classList.remove('pulse'), 500);
                        }

                        // Show Toast Notification
                        showToast(data.message || 'Item added to cart!', 'success');
                    }
                } else {
                    form.submit(); // fallback to regular submit if needed
                }
            } catch (err) {
                console.error('Cart add error:', err);
                form.submit();
            }
        });
    });
});

function showToast(message, type = 'info') {
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.style.position = 'fixed';
        toastContainer.style.bottom = '20px';
        toastContainer.style.right = '20px';
        toastContainer.style.zIndex = '9999';
        document.body.appendChild(toastContainer);
    }

    const toast = document.createElement('div');
    toast.className = `alert-message alert-${type}`;
    toast.style.boxShadow = '0 10px 25px rgba(0,0,0,0.5)';
    toast.style.minWidth = '250px';
    toast.innerHTML = `<i class="bi bi-check-circle-fill"></i> <span>${message}</span>`;

    toastContainer.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.5s ease';
        setTimeout(() => toast.remove(), 500);
    }, 3000);
}
