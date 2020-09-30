from rest_framework import generics, viewsets, filters, mixins
from shop.models import Product
from orders.models import Order, OrderItem
from shop.api.serializers import ProductSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import BasicAuthentication


class ProductListView(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListView(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
