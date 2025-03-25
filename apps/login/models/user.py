from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, email, firstname, lastname, password):
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            firstname=firstname,
            lastname=lastname
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self,username,  email, firstname, lastname, password):
        user = self.create_user(username,email, firstname, lastname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # Pour que l'email soit utilisé comme parametre de connexion
    USERNAME_FIELD = 'email'

    # Paramètres requis a la création du user
    REQUIRED_FIELDS = [
        'firstname',
        'lastname'
    ]

    def __str__(self):
        return f"{self.email}, {self.firstname}, {self.lastname}"
