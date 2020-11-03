from .cart import Cart
from shop.forms import SearchForm


def cart(request):
    return {"cart": Cart(request)}


def product_search(request):
    return {"product_search": SearchForm()}