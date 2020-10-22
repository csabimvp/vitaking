from django.db import models
from django.conf import settings


# ADDRESS_CHOICES = [("S", "Shipping"), ("B", "Billing")]


class Address(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    apartment_address = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    same_billing = models.BooleanField(default=False)
    # address_type = models.CharField(
    # max_length=2, choices=ADDRESS_CHOICES, default="S", unique=True
    # )

    class Meta:
        # unique_together = [["user", "address_type"]]
        verbose_name_plural = "Addresses"
