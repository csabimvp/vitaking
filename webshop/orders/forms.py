from django import forms


class BillingAddressCreateForm(forms.Form):
    same_billing = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "onclick": "myFunction()"}
        )
    )
    billing_street_address = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Számlázási cím, házszám",}
        ),
    )
    billing_apartment_address = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your message..."}
        ),
    )
    billing_postal_code = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Irányítószám"}
        ),
    )
    billing_city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Város"}),
    )

