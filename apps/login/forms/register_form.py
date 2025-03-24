from django import forms
from apps.login.utils.validator import validate_alpha, validate_password_strength

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        required=True,
        label="Nom d'utilisateur",
        validators=[validate_alpha],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Pseudonyme',
                'class': 'form-control text-center mb-2'
            }
        )
    )

    firstname = forms.CharField(
        max_length=50,
        required=True,
        label="Prénom",
        validators=[validate_alpha],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Martin',
                'class': 'form-control text-center mb-2'
            }
        )
    )

    lastname = forms.CharField(
        max_length=50,
        required=True,
        label="Nom",
        validators=[validate_alpha],
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Dupont',
                'class': 'form-control text-center mb-2'
            }
        )
    )

    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                "placeholder": "adresse@contact.com",
                'class': 'form-control text-center mb-2'
            }
        )
    )

    password = forms.CharField(
        required=True,
        label='Mot de passe',
        validators=[validate_password_strength],
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Mon mot de passe",
                'class': 'form-control mb-2 text-center'
            }
        )
    )

    confirm_password = forms.CharField(
        required=True,
        label='Confirmation du mot de passe',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmer mon mot de passe",
                'class': 'form-control text-center mb-2'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and confirm_password != password:
            self.add_error('confirm_password', 'Les mots de passe ne correspondent pas !')

        return cleaned_data

