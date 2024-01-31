from rest_framework import serializers
from .models import *


class ArticleTagSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tag-detail')

    class Meta:
        model = Tag
        fields = '__all__'


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='article-detail')
    tags = ArticleTagSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(ArticleBaseSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ['id', 'url', 'title', 'body', 'tags', 'created']


class ArticleDetailSerializer(ArticleBaseSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        # fields = ['id', 'name', 'url']


class TagDetailSerializer(serializers.ModelSerializer):
    articles = ArticleListSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
        # fields = ['id', 'name', 'articles']
