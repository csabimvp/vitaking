from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "inputCoupon",
                "class": "form-control mr-sm-2",
                "placeholder": "Kupon kód beváltása...",
            }
        ),
        label=False,
    )
