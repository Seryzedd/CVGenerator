from django.db import models
from apps.login.models.user import User
from django.utils.text import slugify

class CVManager():
    def getByUser(self, user):
        return CV.objects.all().filter(user=user).select_related()

    def getByName(self, name):
        return CV.objects.all().filter(name=name).select_related()[0]

class CV(models.Model):
    id = models.CharField(unique=True, primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(max_length=255)
    template = models.CharField(max_length=100)
    primaryColor = models.CharField(max_length=80)
    secondaryColor = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="CVS")

    object = CVManager()

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = "CVS"
        ordering = ['name']

    def update(self, data):
        self.name=data['name']
        self.description = data['description']
        self.template = data['template']
        self.primaryColor = data['primaryColor']
        self.secondaryColor = data['secondaryColor']

        self.save()

        return self

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save()

