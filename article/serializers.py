from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    def check_obj_exist(self, validated_data):
        text = validated_data.get('text')
        if Tag.objects.filter(text=text).exists():
            raise serializers.ValidationError('Tag with text {} exists.'.format(text))
