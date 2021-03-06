from rest_framework import serializers
from shop.models import Product
from orders.models import Order, OrderItem, BillingAddress, ShippingAddress


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "name",
            "slug",
            "image",
            "available",
            "price",
            "on_sale",
            "on_sale_price",
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "product_id",
            "price",
            "quantity",
        ]


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = [
            "billing_street_address",
            "billing_apartment_address",
            "billing_city",
            "billing_postal_code",
        ]


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            "shipping_street_address",
            "shipping_apartment_address",
            "shipping_city",
            "shipping_postal_code",
        ]


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True, read_only=True, source="items")
    billing = BillingAddressSerializer(many=True, read_only=True)
    shipping = ShippingAddressSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "email",
            "paid",
            "payment_method",
            "created",
            "coupon",
            "get_total_cost",
            "shipping",
            "billing",
            "products",
        ]
