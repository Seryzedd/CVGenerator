from django.db import models
from apps.CV.models.CV import CV
from django.utils.text import slugify


class BlockManager():
    def all(self):
        return Block.objects.all()
    def getByCv(self, cv):
        return Block.objects.filter(cv=cv.id)


class Block(models.Model):
    id = models.CharField(unique=True, primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    placement = models.CharField(max_length=50, unique=False, default='')
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="CVS")

    manager = BlockManager()

    class Meta:
        verbose_name = 'Block'
        verbose_name_plural = "Blocks"
        ordering = ['name']

    def update(self, data):
        self.name=data['name']
        self.placement = data['placement']
        self.cv = data['cv']
        if 'id' in data.keys():
            self.id = data['id']

        self.save()

        return self

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save()