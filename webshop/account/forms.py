from django import forms
from django.contrib.auth.models import User
from .models import Address


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "inputUsername",
                "class": "form-control",
                "placeholder": "Felhasználónév",
            }
        ),
        label=False,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "id": "inputPassword",
                "class": "form-control",
                "placeholder": "Jelszó",
            }
        ),
        label=False,
    )


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "id": "inputPassword",
                "class": "form-control",
                "placeholder": "Jelszó",
            }
        ),
        label=False,
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "id": "inputPassword2",
                "class": "form-control",
                "placeholder": "Jelszó",
            }
        ),
        label=False,
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data

        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("A jelszó nem egyezik!")
        return cd["password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email"]


class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "street_address",
            "apartment_address",
            "postal_code",
            "city",
            # "address_type",
        ]

        widgets = {
            "street_address": forms.TextInput(attrs={"class": "form-control"}),
            "apartment_address": forms.TextInput(attrs={"class": "form-control"}),
            "postal_code": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            # "address_type": forms.Select(attrs={"class": "form-control"}),
        }
