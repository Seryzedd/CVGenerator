from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    email = forms.CharField(
        label="Email",
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder' : "email@contact.fr"
            }
        ),

    )
    password = forms.CharField(
        label="Password",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control text-center',
                'placeholder' : "Your password"
            }
        )
    )