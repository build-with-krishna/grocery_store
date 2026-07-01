from django.db import models


class Brand(models.Model):

    name = models.CharField(max_length=100)

    logo = models.ImageField(
        upload_to='brands/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name