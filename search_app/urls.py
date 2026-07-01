from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        search_product,
        name='search_product'
    ),

]