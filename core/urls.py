from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'product/<slug:slug>/',
        product_detail,
        name='product_detail'
    ),

]