from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ProductDescription, ProductImage
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    cart_product_form = CartAddProductForm()

    return render(
        request,
        "shop/product/list.html",
        {
            "category": category,
            "categories": categories,
            "products": products,
            "cart_product_form": cart_product_form,
        },
    )


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()
    descriptors = ProductDescription.objects.filter(
        product_id__in=Product.objects.filter(id=id)
    )
    images = ProductImage.objects.filter(id=id)

    similar_products = Product.objects.filter(category=product.category).exclude(id=id)
    similar_products = similar_products[:4]

    cart_product_form = CartAddProductForm()

    return render(
        request,
        "shop/product/detail.html",
        {
            "product": product,
            "categories": categories,
            "similar_products": similar_products,
            "cart_product_form": cart_product_form,
            "descriptors": descriptors,
            "images": images,
        },
    )


def home_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(
        request,
        "shop/index.html",
        {"category": category, "categories": categories, "products": products},
    )


def on_sale_view(request):
    products = Product.objects.filter(on_sale=True)
    categories = Category.objects.all()

    cart_product_form = CartAddProductForm()

    return render(
        request,
        "shop/product/sale.html",
        {
            "products": products,
            "categories": categories,
            "cart_product_form": cart_product_form,
        },
    )
