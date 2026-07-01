from rest_framework import generics

from products.models import Product
from category.models import Category

from .serializers import (
    ProductSerializer,
    CategorySerializer
)


class ProductListAPIView(

    generics.ListAPIView

):

    queryset = Product.objects.filter(
        is_active=True,
        is_approved=True
    )

    serializer_class = ProductSerializer


class ProductDetailAPIView(

    generics.RetrieveAPIView

):

    queryset = Product.objects.filter(
        is_active=True,
        is_approved=True
    )

    serializer_class = ProductSerializer


class CategoryListAPIView(

    generics.ListAPIView

):

    queryset = Category.objects.filter(
        is_active=True
    )

    serializer_class = CategorySerializer