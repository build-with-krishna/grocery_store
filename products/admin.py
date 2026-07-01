from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):

    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'vendor',
        'price',
        'stock',
        'is_active',
        'is_approved'
    ]

    list_filter = [
        'is_active',
        'is_approved'
    ]

    prepopulated_fields = {
        'slug': ('name',)
    }

    inlines = [ProductImageInline]
