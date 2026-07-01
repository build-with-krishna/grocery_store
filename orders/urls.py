from django.urls import path
from .views import *

urlpatterns = [

    path(
        'checkout/',
        checkout,
        name='checkout'
    ),

    path(
        'my-orders/',
        my_orders,
        name='my_orders'
    ),

    path(
        'detail/<int:id>/',
        order_detail,
        name='order_detail'
    ),

]