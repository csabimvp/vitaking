from django import forms
from django.contrib.auth.models import User


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
                "id": "inputPassword",
                "class": "form-control",
                "placeholder": "Jelszó",
            }
        ),
        label=False,
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data

        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("A jelszó nem egyezik!")
        return cd["password2"]

