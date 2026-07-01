from django.urls import path
from .views import *

urlpatterns = [

    path(
        '<int:order_id>/',
        payment_method,
        name='payment_method'
    ),

    path(
        'verify/',
        verify_payment,
        name='verify_payment'
    ),

    path(
        'success/',
        payment_success,
        name='payment_success'
    ),

    path(
        'failed/',
        payment_failed,
        name='payment_failed'
    ),
]