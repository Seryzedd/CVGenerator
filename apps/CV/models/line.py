from django.db import models
from apps.CV.models import Block
from apps.login.models.user import User
from django.utils.text import slugify

class LineManager():
    def all(self):
        return Line.objects.all()

    def getByBlocks(self, blockIds):
        return Line.objects.filter(block__in=blockIds)

class Line(models.Model):
    title = models.CharField(max_length=50, unique=False)
    startAt = models.DateTimeField(unique=False, blank=True, default=None, null=True)
    endAt = models.DateTimeField(unique=False, blank=True, default=None, null=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="blocks")

    class Meta:
        verbose_name = 'Line'
        verbose_name_plural = "Lines"
        ordering = ['title']

    def update(self, data):
        if 'title' in data.keys():
            self.title=data['title']
        if 'startAt' in data.keys() and data['startAt'] != "":
            self.startAt = data['startAt']
        if 'endAt' in data and data['endAt'] != "":
            self.endAt = data['endAt']
        self.block = data['block']

        self.save()

        return self