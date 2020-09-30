from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("termekek/", views.product_list, name="product_list"),
    path("sale/", views.on_sale_view, name="on_sale_view"),
    path("<slug:category_slug>/", views.product_list, name="product_list_by_category"),
    path("<int:id>/<slug:slug>/", views.product_detail, name="product_detail"),
]
