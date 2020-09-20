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
        "address_type",
        "default",
    ]

    list_filter = ["default", "address_type", "city"]
    search_fields = ["user", "street_address", "apartment_address"]
