from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "street_address",
        "apartment_address",
        "postal_code",
        "city",
        "phone_number"
        # "address_type",
    ]

    list_filter = ["user", "city"]
    search_fields = ["user", "street_address", "apartment_address"]
