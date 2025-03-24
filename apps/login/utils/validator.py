from django.core.exceptions import ValidationError
import re

def validate_alpha(value):
    """
    Valider que le champ contien uniquement des lettres
    :param value:
    :return:
    """
    if not value.isalpha():
        raise ValidationError("Ce champ doit contenir uniquement des lettres")

def validate_password_strength(value):
    """
    Valider la force du mot de passe
    :param value:
    :return:
    """

    if len(value) < 8:
        raise ValidationError('Le mot de passe doit contenir au moins 8 caractères')
    if not re.search(r"[A-Z]", value):
        raise ValidationError("Le mot de passe doit contenir au moins une majuscule")
    if not re.search(r"[a-z]", value):
        raise ValidationError("Le mot de passe doit contenir au moins une minuscule")
    if not re.search(r"\d", value):
        raise ValidationError("Le mot de passe doit contenir au moins un chiffre")
    if not re.search(r"[!@#$%^*&():?]", value):
        raise ValidationError("Le mot de passe doit contenir au moins un caractère spécial")

