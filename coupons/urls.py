from django.urls import path
from .views import *

urlpatterns = [

    path(
        'apply/',
        apply_coupon,
        name='apply_coupon'
    ),

]