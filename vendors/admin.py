from django.contrib import admin
from .models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):

    list_display = (
        'shop_name',
        'user',
        'gst_number',
        'is_approved'
    )

    list_filter = ('is_approved',)