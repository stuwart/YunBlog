from django.db import models
from markdown import markdown


# Create your models here.

class Tag(models.Model):
    text = models.CharField(max_length=30)

    class meta:
        ordering = ['-id']

    def __str__(self):
        return self.text

class Avator(models.Model):
    content = models.ImageField(upload_to='')