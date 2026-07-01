from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone

from .models import Coupon, CouponUsage


def apply_coupon(request):

    if request.method == "POST":

        code = request.POST.get('coupon_code')

        total = float(
            request.session.get(
                'checkout_total',
                0
            )
        )

        try:

            coupon = Coupon.objects.get(
                code=code,
                is_active=True
            )

        except Coupon.DoesNotExist:

            messages.error(
                request,
                "Invalid Coupon"
            )

            return redirect('/orders/checkout/')

        if coupon.expiry_date < timezone.now().date():

            messages.error(
                request,
                "Coupon Expired"
            )

            return redirect('/orders/checkout/')

        already_used = CouponUsage.objects.filter(
            user=request.user,
            coupon=coupon
        ).exists()

        if already_used:

            messages.error(
                request,
                "Coupon already used"
            )

            return redirect('/orders/checkout/')

        if total < coupon.minimum_amount:

            messages.error(
                request,
                "Minimum order amount not reached"
            )

            return redirect('/orders/checkout/')

        if coupon.discount_type == "percentage":

            discount = (
                total *
                float(coupon.discount_value)
            ) / 100

        else:

            discount = float(
                coupon.discount_value
            )

        request.session['discount'] = discount
        request.session['coupon_code'] = coupon.code

        messages.success(
            request,
            "Coupon Applied Successfully"
        )

    return redirect('/orders/checkout/')