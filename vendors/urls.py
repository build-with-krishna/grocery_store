from django.urls import path
from .views import vendor_register, vendor_dashboard

urlpatterns = [

    path('register/', vendor_register, name='vendor_register'),

    path(
        'dashboard/',
        vendor_dashboard,
        name='vendor_dashboard'
    ),

]