from django.shortcuts import render, redirect
from .models import OrderItem, Order, BillingAddress
from .forms import BillingAddressCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.models import User
from account.models import Address
from coupons.models import Coupon
from .tasks import order_created
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
import weasyprint


@login_required
def order_create(request):
    cart = Cart(request)
    usr = request.user.id
    user = User.objects.get(id=usr)

    try:
        address = Address.objects.get(user_id=user)
    except Address.DoesNotExist:
        address = None

    if request.method == "POST":
        form = BillingAddressCreateForm(
            request.POST,
            initial={
                "billing_street_address": address.street_address,
                "billing_apartment_address": address.apartment_address,
                "billing_city": address.city,
                "billing_postal_code": address.postal_code,
            },
        )

        if cart.coupon == None:
            disc = 0
        else:
            disc = cart.coupon.discount

        if form.is_valid():
            Order.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                address=address.street_address,
                address2=address.apartment_address,
                postal_code=address.postal_code,
                city=address.city,
                coupon=cart.coupon,
                discount=disc,
            )

            order = Order.objects.latest("id")

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            if form.cleaned_data["same_billing"] == True:
                BillingAddress.objects.create(
                    order=order,
                    billing_street_address=address.street_address,
                    billing_apartment_address=address.apartment_address,
                    billing_city=address.city,
                    billing_postal_code=address.postal_code,
                )
            else:
                BillingAddress.objects.create(
                    order=order,
                    billing_street_address=form.cleaned_data["billing_street_address"],
                    billing_apartment_address=form.cleaned_data[
                        "billing_apartment_address"
                    ],
                    billing_city=form.cleaned_data["billing_city"],
                    billing_postal_code=form.cleaned_data["billing_postal_code"],
                )

            cart.clear()
            # launch asynchronus task
            # order_created.delay(order.id)
            request.session["order_id"] = order.id
            # redirect for payment
            return redirect(reverse("payment:process"))

    else:
        form = BillingAddressCreateForm()

    return render(
        request,
        "orders/order/create.html",
        {"cart": cart, "form": form, "user": user, "address": address},
    )


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string("orders/order/pdf.html", {"order": order})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=rendeles_{order.id}.pdf"
    weasyprint.HTML(string=html).write_pdf(
        response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + "css/pdf.css")]
    )
    return response
