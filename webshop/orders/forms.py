from django import forms

CHOICES = [("1", "Hitelkártya"), ("2", "Bankkártya"), ("3", "Postai utánvétel")]


class BillingAddressCreateForm(forms.Form):
    same_billing = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "onclick": "myFunction()"}
        ),
    )

    payment_method = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input", "type": "radio"}),
    )

    billing_street_address = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Számlázási cím, házszám"}
        ),
    )
    billing_apartment_address = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Emelet, ajtószám"}
        ),
    )
    billing_postal_code = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Irányítószám"}
        ),
    )
    billing_city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Város"}),
    )

    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+36308535626"}
        ),
    )


class OrderCreateForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Keresztnév"}
        ),
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Vezetéknév"}
        ),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "valami@gmail.com"}
        ),
    )

    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "+36308535626"}
        ),
    )

    same_billing = forms.BooleanField(
        initial=False,
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "onclick": "myFunction()"}
        ),
    )

    payment_method = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input", "type": "radio"}),
    )

    shipping_street_address = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Szállítási cím, házszám"}
        ),
    )
    shipping_apartment_address = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Emelet, ajtószám"}
        ),
    )
    shipping_postal_code = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Irányítószám"}
        ),
    )
    shipping_city = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Város"}),
    )

    billing_street_address = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Számlázási cím, házszám"}
        ),
    )
    billing_apartment_address = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Emelet, ajtószám"}
        ),
    )
    billing_postal_code = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Irányítószám"}
        ),
    )
    billing_city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Város"}),
    )
