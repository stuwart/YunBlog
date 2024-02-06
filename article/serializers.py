from rest_framework import serializers
from .models import *


# class ArticleTagSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='tag-detail')
#
#     class Meta:
#         model = Tag
#         fields = '__all__'


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name='article-detail')
    id = serializers.IntegerField(read_only=True)
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='name',
        allow_null=True
    )

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = Article.objects.create(**validated_data)
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        return instance

    def update(self, instance, validated_data):
        instance.tags.clear()  # Optional: Clear existing tags and replace with new ones
        tags_data = validated_data.pop('tags', [])
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        return super().update(instance, validated_data)

    def to_internal_value(self, data):
        tags_data = data.get('tags')

        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(name=text).exists():
                    Tag.objects.create(name=text)

        return super().to_internal_value(data)
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
