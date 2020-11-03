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
