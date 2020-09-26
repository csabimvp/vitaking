from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .tasks import order_created


@login_required
def order_create(request):
    cart = Cart(request)
    usr = request.user.id
    user = User.objects.get(id=usr)

    if request.method == "POST":
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            form.instance.user = user
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            cart.clear()
            # launch asynchronus task
            # order_created.delay(order.id)

            return render(request, "orders/order/created.html", {"order": order})

    else:
        form = OrderCreateForm()

    return render(request, "orders/order/create.html", {"cart": cart, "form": form})
