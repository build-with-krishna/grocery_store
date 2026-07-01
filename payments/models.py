from django.db import models
from orders.models import Order


class Payment(models.Model):

    METHOD_CHOICES = (
        ('COD', 'Cash On Delivery'),
        ('RAZORPAY', 'Razorpay'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE
    )

    payment_method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES
    )

    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    razorpay_order_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.order_number