from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'category',
            'brand',
            'name',
            'slug',
            'sku',
            'barcode',
            'description',
            'price',
            'discount_price',
            'stock',
            'thumbnail',
        ]