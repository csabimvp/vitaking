from django.contrib import admin
from .models import Address, BillingAddress


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "street_address",
        "apartment_address",
        "postal_code",
        "city",
        "same_billing"
        # "address_type",
    ]

    list_filter = ["user", "city"]
    search_fields = ["user", "street_address", "apartment_address"]


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "billing_street_address",
        "billing_apartment_address",
        "billing_postal_code",
        "billing_city",
        # "address_type",
    ]

    list_filter = ["user", "billing_city"]
    search_fields = ["user", "billing_street_address", "billing_apartment_address"]
