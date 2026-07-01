import razorpay

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from orders.models import Order
from .models import Payment


client = razorpay.Client(
    auth=(
        settings.RAZORPAY_KEY_ID,
        settings.RAZORPAY_KEY_SECRET
    )
)


def payment_method(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":

        method = request.POST.get('payment_method')

        # COD
        if method == "COD":

            payment, created = Payment.objects.get_or_create(
                order=order,
                defaults={
                    'payment_method': 'COD',
                    'amount': order.total_amount,
                    'status': 'success'
                }
            )

            if not created:
                payment.payment_method = 'COD'
                payment.amount = order.total_amount
                payment.status = 'success'
                payment.save()

            order.status = "confirmed"
            order.save()

            return redirect('/payments/success/')

        # Razorpay
        if method == "RAZORPAY":

            amount = int(order.total_amount * 100)

            razorpay_order = client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture": "1"
            })

            payment, created = Payment.objects.get_or_create(
                order=order,
                defaults={
                    'payment_method': 'RAZORPAY',
                    'amount': order.total_amount,
                    'razorpay_order_id': razorpay_order['id']
                }
            )

            if not created:
                payment.payment_method = 'RAZORPAY'
                payment.amount = order.total_amount
                payment.razorpay_order_id = razorpay_order['id']
                payment.status = 'pending'
                payment.save()

            context = {
                "order": order,
                "razorpay_order_id": razorpay_order['id'],
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "amount": amount
            }

            return render(
                request,
                "payments/razorpay_checkout.html",
                context
            )

    return render(
        request,
        "payments/payment_method.html",
        {
            "order": order
        }
    )


@csrf_exempt
def verify_payment(request):

    if request.method == "POST":

        payment_id = request.POST.get(
            'razorpay_payment_id'
        )

        razorpay_order_id = request.POST.get(
            'razorpay_order_id'
        )

        signature = request.POST.get(
            'razorpay_signature'
        )

        params = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:

            client.utility.verify_payment_signature(
                params
            )

            payment = Payment.objects.get(
                razorpay_order_id=razorpay_order_id
            )

            payment.transaction_id = payment_id
            payment.status = "success"
            payment.save()

            order = payment.order
            order.status = "confirmed"
            order.save()

            return redirect('/payments/success/')

        except:

            return redirect('/payments/failed/')


def payment_success(request):

    return render(
        request,
        'payments/payment_success.html'
    )


def payment_failed(request):

    return render(
        request,
        'payments/payment_failed.html'
    )