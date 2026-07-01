from django.db import models
from accounts.models import User


class Coupon(models.Model):

    DISCOUNT_TYPE = (
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed Amount'),
    )

    code = models.CharField(
        max_length=50,
        unique=True
    )

    discount_type = models.CharField(
        max_length=20,
        choices=DISCOUNT_TYPE
    )

    discount_value = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    minimum_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    expiry_date = models.DateField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class CouponUsage(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    coupon = models.ForeignKey(
        Coupon,
        on_delete=models.CASCADE
    )

    used_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ['user', 'coupon']