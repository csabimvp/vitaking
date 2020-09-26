from django.urls import path
from shop.api.views import ProductListView, OrderListView, OrderItemListView
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"products", ProductListView, basename="product_list")
router.register(r"orders", OrderListView, basename="order_list")
router.register(r"orderitems", OrderItemListView, basename="order_items")

app_name = "shop"

urlpatterns = [
    # path("products/", ProductListView, name="product_list"),
    # path("products/<pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    # path("orders/", OrderListView, name="order_list"),
    # path("orders/<pk>/", views.OrderDetailView.as_view(), name="order_detail"),
    url(r"^v1/", include(router.urls)),
]
