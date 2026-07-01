from django.db import models
from accounts.models import User


class Vendor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    shop_name = models.CharField(max_length=200)

    gst_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    pan_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    bank_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    account_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    ifsc_code = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shop_name