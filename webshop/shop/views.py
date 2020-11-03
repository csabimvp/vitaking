from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from .models import Category, Product, ProductDescription, ProductImage
from cart.forms import CartAddProductForm
from .recommender import Recommender
from .forms import SearchForm


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

    on_sale_products = Product.objects.filter(on_sale=True).exclude(id=id)
    on_sale_products = on_sale_products[:4]

    cart_product_form = CartAddProductForm()

    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    return render(
        request,
        "shop/product/detail.html",
        {
            "product": product,
            "categories": categories,
            "on_sale_products": on_sale_products,
            "cart_product_form": cart_product_form,
            "descriptors": descriptors,
            "images": images,
            "recommended_products": recommended_products,
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


def contact_view(request):
    categories = Category.objects.all()

    return render(
        request,
        "shop/contact.html",
        {"categories": categories},
    )


def about_view(request):
    categories = Category.objects.all()

    return render(
        request,
        "shop/about.html",
        {"categories": categories},
    )


def product_search(request):
    form = SearchForm()
    query = None
    results = []

    categories = Category.objects.all()

    if "query" in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Product.objects.annotate(
                search=SearchVector("name", "description"),
            ).filter(search=query)

    return render(
        request,
        "shop/kereses.html",
        {"categories": categories, "form": form, "query": query, "results": results},
    )
