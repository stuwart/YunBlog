from django.db.models import Count
from django.shortcuts import render
from rest_framework import views, serializers, viewsets, filters
from rest_framework import generics
from article.models import Tag, Article
from .serializers import *


class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        # 注入每个标签的文章计数并按该计数降序排序
        return Tag.objects.annotate(cnt=Count('articles')).order_by('-cnt')


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
