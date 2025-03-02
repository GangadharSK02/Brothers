# contents/api/serializers.py

from rest_framework import serializers
from contents.models import TextContent, VideoContent, FileContent

class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = '__all__'

class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = '__all__'

class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileContent
        fields = '__all__'
