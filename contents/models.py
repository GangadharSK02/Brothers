#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduPlatform.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()


from django.db import models
from courses.models import Lesson

# Abstract base model for lesson content
class LessonContent(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="%(class)ss")
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    publish_date = models.DateTimeField(null=True, blank=True)  # Content scheduling
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['order']

# ---------- Text-based Content ----------
class TextContent(LessonContent):
    text = models.TextField()

    def __str__(self):
        return f"Text: {self.title}"

# ---------- Video Content ----------
class VideoContent(LessonContent):
    video_url = models.URLField(help_text="URL of the video content")

    def __str__(self):
        return f"Video: {self.title}"

# ---------- File Attachment (PDFs etc.) ----------
class FileContent(LessonContent):
    file = models.FileField(upload_to='attachments/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"File: {self.title}"
