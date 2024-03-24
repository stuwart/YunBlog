from django.utils import timezone
from django.db import models
from markdown import Markdown


class Tag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Article(models.Model):
    # related_name:可以通过tags.articles.all()访问所有的对应文章
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        # toc 是渲染后的目录
        return md_body, md.toc

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title
