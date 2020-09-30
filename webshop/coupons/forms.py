from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "inputCoupon",
                "class": "form-control",
                "placeholder": "Kupon kód",
            }
        ),
        label=False,
    )
