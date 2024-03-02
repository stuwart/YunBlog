from django.db.models import Count
from django.shortcuts import render
from rest_framework import views, serializers, viewsets, filters
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from article.models import Tag, Article
from .serializers import *


class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer

    def get_queryset(self):
        # 注入每个标签的文章计数并按该计数降序排序
        return Tag.objects.annotate(cnt=Count('articles')).order_by('-cnt')


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer


class ArticleByTagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = ArticleTagSerializer

    def get_queryset(self):
        tag_id = self.kwargs['pk']  # 从URL捕获的参数
        tag = get_object_or_404(Tag, pk=tag_id)  # 确保标签存在
        return tag.articles.all()


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
