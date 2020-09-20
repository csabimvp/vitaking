from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm
from orders.models import Order
from .models import Address
from django.shortcuts import get_object_or_404


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")

                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            # Create new User object but avoid saving it yet.
            new_user = user_form.save(commit=False)

            # Set the chosen password
            new_user.set_password(user_form.cleaned_data["password"])

            # Save the user object
            new_user.save()

            username = user_form.cleaned_data["username"]
            messages.success(request, f"Sikeres regisztráció {username}!")

            return render(request, "account/register_done.html", {"new_user": new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request, "account/register.html", {"user_form": user_form})


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    # address = get_object_or_404(Address, user=user)
    address = Address.objects.filter(user__in=User.objects.filter(username=username))
    shipping_address = address.filter(address_type="s")
    billing_address = address.filter(address_type="b")
    # orders = get_object_or_404(Order, user=user)
    return render(
        request,
        "account/user/detail.html",
        {
            "user": user,
            "address": address,
            "shipping_address": shipping_address,
            "billing_address": billing_address,
        },
    )

    # return render(request, "account/user/detail.html", {"user": user})
