from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "addtocartform",
            }
        ),
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label="Mennyiség",
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )


class CartAddSingleProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "exampleFormControlSelect1",
                "onchange": "this.form.submit()",
            }
        ),
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
