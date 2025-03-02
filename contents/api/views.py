# contents/api/views.py

from rest_framework import viewsets
from contents.models import TextContent, VideoContent, FileContent
from .serializers import TextContentSerializer, VideoContentSerializer, FileContentSerializer

class TextContentViewSet(viewsets.ModelViewSet):
    queryset = TextContent.objects.all()
    serializer_class = TextContentSerializer

class VideoContentViewSet(viewsets.ModelViewSet):
    queryset = VideoContent.objects.all()
    serializer_class = VideoContentSerializer

class FileContentViewSet(viewsets.ModelViewSet):
    queryset = FileContent.objects.all()
    serializer_class = FileContentSerializer
