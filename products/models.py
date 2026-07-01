from django.db import models
from vendors.models import Vendor
from category.models import Category
from brands.models import Brand


class Product(models.Model):

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    sku = models.CharField(
        max_length=100,
        unique=True
    )

    barcode = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(default=0)

    thumbnail = models.ImageField(
        upload_to='products/'
    )

    is_active = models.BooleanField(default=True)

    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='product_gallery/'
    )

    def __str__(self):
        return self.product.name