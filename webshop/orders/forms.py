from django import forms


class BillingAddressCreateForm(forms.Form):
    same_billing = forms.BooleanField()
    billing_street_address = forms.CharField(max_length=200)
    billing_apartment_address = forms.CharField(max_length=100)
    billing_postal_code = forms.CharField(max_length=30)
    billing_city = forms.CharField(max_length=100)
