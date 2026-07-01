import uuid
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from .models import Order, OrderItem


@login_required
def checkout(request):

    cart = Cart.objects.get(user=request.user)

    items = cart.items.all()

    total = 0

    for item in items:
        total += item.subtotal

    # Coupon
    request.session['checkout_total'] = str(total)

    discount = Decimal(
        str(
            request.session.get(
                'discount',
                0
            )
        )
    )

    final_total = total - discount

    if final_total < 0:
        final_total = Decimal('0')

    if final_total < 0:
        final_total = 0

    if request.method == "POST":

        order = Order.objects.create(
            user=request.user,
            order_number=str(uuid.uuid4())[:8].upper(),
            full_name=request.POST['full_name'],
            mobile=request.POST['mobile'],
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            pincode=request.POST['pincode'],
            total_amount=final_total
        )

        for item in items:

            price = item.product.discount_price or item.product.price

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=price,
                subtotal=item.subtotal
            )

            # Stock Update
            item.product.stock -= item.quantity
            item.product.save()

        # Coupon Usage Save
        from coupons.models import Coupon, CouponUsage

        coupon_code = request.session.get('coupon_code')

        if coupon_code:

            try:

                coupon = Coupon.objects.get(
                    code=coupon_code
                )

                CouponUsage.objects.get_or_create(
                    user=request.user,
                    coupon=coupon
                )

            except Coupon.DoesNotExist:
                pass

            request.session.pop(
                'coupon_code',
                None
            )

            request.session.pop(
                'discount',
                None
            )

        items.delete()

        return redirect(
            f'/payments/{order.id}/'
        )

    return render(
        request,
        'orders/checkout.html',
        {
            'items': items,
            'total': total,
            'discount': discount,
            'final_total': final_total,
        }
    )


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'orders/my_orders.html',
        {
            'orders': orders
        }
    )


@login_required
def order_detail(request, id):

    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    return render(
        request,
        'orders/order_detail.html',
        {
            'order': order
        }
    )