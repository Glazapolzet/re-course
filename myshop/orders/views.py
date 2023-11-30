from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})


def order_create(request):
    cart = Cart(request)

    if not request.method == 'POST':
        form = OrderCreateForm
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

    form = OrderCreateForm(request.POST)
    
    if not form.is_valid():
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

    order = form.save(commit=False)

    if cart.coupon:
        order.coupon = cart.coupon
        order.discount = cart.coupon.discount
    order.save()

    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity']
        )
    cart.clear()
    order_created.delay(order.id)
    
    return render(request, 'orders/order/created.html', {'order': order})
