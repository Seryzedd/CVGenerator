from django.db import models

class AdressManager():
    def getAll(self):
        return Adress.objects.all()

    def getByUser(self, user):
        return Adress.objects.filter(id=user.id)

class Adress(models.Model):
    street = models.CharField(max_length=100, unique=False, default='')
    city = models.CharField(max_length=100, unique=False, default='')
    zipCode = models.CharField(max_length=10, unique=False, default='')
    country = models.CharField(max_length=50, unique=False, default='France')

    def update(self, data):
        self.street=data['street']
        self.city=data['city']
        self.zipCode=data['zipCode']
        self.country=data['country']

        super().save()
        return self

