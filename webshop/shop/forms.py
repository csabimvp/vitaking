from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "searchfield",
                "class": "form-control mr-sm-2",
                "placeholder": "Keresés...",
            }
        ),
        label=False,
    )