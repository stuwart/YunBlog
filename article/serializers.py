from rest_framework import serializers
from .models import *


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='article-detail')
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='name'
    )

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


# 嵌套序列化器
class TagArticleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = '__all__'


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        # fields = ['id', 'name', 'url']


class TagDetailSerializer(serializers.ModelSerializer):
    articles = TagArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
        # fields = ['id', 'name', 'articles']
