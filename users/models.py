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
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    gamification_points = models.IntegerField(default=0)
    badges = models.JSONField(default=list, blank=True)  # a list of badge identifiers/names
    preferred_language = models.CharField(max_length=20, default='en')
    # For personalized learning paths we store an ordered list (e.g., lesson IDs)
    personalized_learning_path = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
