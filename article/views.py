from django.shortcuts import render
from rest_framework import views, serializers, viewsets
from rest_framework import generics
from article.models import *
from article.serializers import *


# Create your views here.

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):  # 在真正保存前执行此步骤
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer
