from django.utils import timezone
from django.db import models
from markdown import Markdown

class Tag(models.Model):
    text = models.CharField(max_length=30)

    class meta:
        ordering = ['-id']

    def __str__(self):
        return self.text


class Avatar(models.Model):
    image = models.ImageField(upload_to='avatar/%Y%m%d')


class Article(models.Model):
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    avatar = models.ForeignKey(Avatar, null=True, blank=True, on_delete=models.SET_NULL, related_name='article')
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        return md_body
