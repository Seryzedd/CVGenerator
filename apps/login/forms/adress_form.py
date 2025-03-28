from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AdressForm(forms.Form):
    street = forms.CharField(
        max_length=50,
        required=True,
        label="Rue",
        validators=[],
        widget=forms.TextInput(
            attrs={
                'placeholder': '',
                'class': 'form-control text-center mb-2'
            }
        )
    )

    city = forms.CharField(
        max_length=50,
        required=True,
        label="Ville",
        validators=[],
        widget=forms.TextInput(
            attrs={
                'placeholder': '',
                'class': 'form-control text-center mb-2'
            }
        )
    )

    zipCode = forms.CharField(
        max_length=50,
        required=True,
        label="Code postale",
        validators=[],
        widget=forms.TextInput(
            attrs={
                'placeholder': '',
                'class': 'form-control text-center mb-2'
            }
        )
    )

    country = forms.CharField(
        max_length=50,
        required=True,
        label="Pays",
        validators=[],
        widget=forms.TextInput(
            attrs={
                'placeholder': '',
                'class': 'form-control text-center mb-2'
            }
        )
    )

    def setData(self, user):
        self.initial['street']=user.adress.street
        self.initial['city'] = user.adress.city
        self.initial['zipCode'] = user.adress.zipCode
        self.initial['country'] = user.adress.country