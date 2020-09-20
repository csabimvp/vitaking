from django.db import models
from django.conf import settings

ADDRESS_CHOICES = [("S", "Shipping"), ("B", "Billing")]


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    address_type = models.CharField(
        max_length=1, choices=ADDRESS_CHOICES, default=False
    )
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return str(self.id)
