from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    CUSTOMER = "customer"
    VENDOR = "vendor"

    ROLE_CHOICES = (
        (CUSTOMER, "Customer"),
        (VENDOR, "Vendor"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER
    )

    mobile = models.CharField(max_length=15, blank=True, null=True)

    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username