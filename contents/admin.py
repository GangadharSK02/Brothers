from django.contrib import admin
from .models import TextContent, VideoContent, FileContent

admin.site.register(TextContent)
admin.site.register(VideoContent)
admin.site.register(FileContent)
