from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserUpdateForm, AddressUpdateForm
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
                    messages.success(request, f"Üdv újra {request.user.first_name}!")
                    # return HttpResponse("Authenticated successfully")

                else:
                    messages.warning(request, f"Érvénytelen bejelentkezés.")
                    return render(request, "account/login.html", {"form": form})
            else:
                messages.warning(request, f"Érvénytelen bejelentkezés.")
                return render(request, "account/login.html", {"form": form})
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

            name = user_form.cleaned_data["first_name"]
            messages.success(request, f"Sikeres regisztráció {name}!")

            return render(request, "account/register_done.html", {"new_user": new_user})

    else:
        user_form = UserRegistrationForm()

    return render(request, "account/register.html", {"user_form": user_form})


@login_required
def duser_profile(request):
    username = request.user.username
    user = User.objects.get(username=username)
    # address = get_object_or_404(Address, user=user)
    address = Address.objects.filter(user__in=User.objects.filter(username=username))
    shipping_address = address.filter(address_type="s")
    billing_address = address.filter(address_type="b")
    # orders = get_object_or_404(Order, user=user)

    return render(
        request,
        "account/detail.html",
        {
            "user": user,
            "address": address,
            "shipping_address": shipping_address,
            "billing_address": billing_address,
        },
    )


@login_required
def user_profile_edit(request):
    if request.method == "POST":

        user = request.user.id
        addr, created = Address.objects.get_or_create(user_id=user)

        if created:
            a_form = AddressUpdateForm(user, request.POST)

            if a_form.is_valid():
                a_form.save()
                messages.success(
                    request,
                    f"Változtatások sikeresen elmentve {request.user.first_name}!",
                )
                return redirect("account:user_profile")

        else:
            a_form = AddressUpdateForm(request.POST, instance=addr)

            if a_form.is_valid():
                a_form.save()
                messages.success(
                    request,
                    f"Változtatások sikeresen elmentve {request.user.first_name}!",
                )
                return redirect("account:user_profile")

    else:
        a_form = AddressUpdateForm()

    return render(request, "account/edit.html", {"a_form": a_form})


@login_required
def user_profile(request):
    username = request.user.username
    user = User.objects.get(username=username)
    # address = get_object_or_404(Address, user=user)
    address = Address.objects.filter(user__in=User.objects.filter(username=username))
    # shipping_address = address.filter(address_type="s")
    # billing_address = address.filter(address_type="b")
    # orders = get_object_or_404(Order, user=user)
    if request.method == "POST":
        try:
            usr = request.user.id
            addr = Address.objects.get(user_id=usr)

            a_form = AddressUpdateForm(request.POST, instance=addr)

            if a_form.is_valid():
                a_form.save()
                messages.success(
                    request,
                    f"Változtatások sikeresen elmentve {request.user.first_name}!",
                )
                return redirect("account:user_profile")

        except Address.DoesNotExist:
            a_form = AddressUpdateForm(request.POST)

            if a_form.is_valid():
                a_form.instance.user = user
                a_form.save()
                messages.success(
                    request,
                    f"Változtatások sikeresen elmentve {request.user.first_name}!",
                )
                return redirect("account:user_profile")

    else:
        a_form = AddressUpdateForm()

    return render(
        request,
        "account/detail.html",
        {
            "user": user,
            "address": address,
            # "shipping_address": shipping_address,
            # "billing_address": billing_address,
            "a_form": a_form,
        },
    )
