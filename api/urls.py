from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (

    TokenObtainPairView,
    TokenRefreshView

)

urlpatterns = [

    path(
        'token/',
        TokenObtainPairView.as_view()
    ),

    path(
        'token/refresh/',
        TokenRefreshView.as_view()
    ),

    path(
        'products/',
        ProductListAPIView.as_view()
    ),

    path(
        'products/<int:pk>/',
        ProductDetailAPIView.as_view()
    ),

    path(
        'categories/',
        CategoryListAPIView.as_view()
    ),

]