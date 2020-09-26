from django.contrib import admin
from .models import Category, Product, ProductDescription, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


class ProductDescriptionAdmin(admin.StackedInline):
    model = ProductDescription


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductDescriptionAdmin, ProductImageAdmin]

    list_display = ["name", "slug", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated", "on_sale"]
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Product


@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_filter = ["product"]

    class Meta:
        model = ProductImage
