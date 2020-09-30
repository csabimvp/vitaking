from rest_framework import serializers
from shop.models import Product
from orders.models import Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
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


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True, read_only=True, source="items")

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "email",
            "city",
            "address",
            "address2",
            "postal_code",
            "same_billing",
            "paid",
            "created",
            "coupon",
            "get_total_cost",
            "products",
        ]
