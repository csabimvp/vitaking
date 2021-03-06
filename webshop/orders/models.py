from django.db import models
from shop.models import Product
from django.conf import settings
from account.models import Address
from coupons.models import Coupon
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=False
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50)
    coupon = models.ForeignKey(
        Coupon, related_name="orders", null=True, blank=True, on_delete=models.SET_NULL
    )
    discount = models.IntegerField(default=0)
    braintree_id = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        # total_cost = sum(item.get_cost() for item in self.items.all())
        total_cost = sum(
            item.get_onsale_cost() if item.product.on_sale == True else item.get_cost()
            for item in self.items.all()
        )
        return total_cost - total_cost * (self.discount / Decimal(100))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def sale(self):
        return self.product.on_sale

    def get_cost(self):
        return self.price * self.quantity

    def get_onsale_cost(self):
        return self.product.on_sale_price * self.quantity


class BillingAddress(models.Model):
    order = models.ForeignKey(Order, related_name="billing", on_delete=models.CASCADE)
    billing_street_address = models.CharField(max_length=200)
    billing_apartment_address = models.CharField(max_length=100, blank=True)
    billing_postal_code = models.CharField(max_length=30)
    billing_city = models.CharField(max_length=100)
    phone_number = PhoneNumberField()

    def __str__(self):
        return str(self.id)


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, related_name="shipping", on_delete=models.CASCADE)
    shipping_street_address = models.CharField(max_length=200)
    shipping_apartment_address = models.CharField(max_length=100, blank=True)
    shipping_postal_code = models.CharField(max_length=30)
    shipping_city = models.CharField(max_length=100)
    phone_number = PhoneNumberField()

    def __str__(self):
        return str(self.id)
