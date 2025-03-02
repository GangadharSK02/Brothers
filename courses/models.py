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
from django.contrib.auth import get_user_model

User = get_user_model()

# -------------------------------------------------------------------
# Course classification models
# -------------------------------------------------------------------
class CourseLevel(models.Model):
    name = models.CharField(max_length=50)  # e.g., Beginner, Intermediate, Advanced

    def __str__(self):
        return self.name

class CourseCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# -------------------------------------------------------------------
# Main Course and its structure
# -------------------------------------------------------------------
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.ForeignKey(CourseLevel, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    # Monetization: free courses but require a mentor-signed agreement
    agreement_required = models.BooleanField(default=True)
    mentor_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} > {self.title}"

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.module.title} > {self.title}"

# -------------------------------------------------------------------
# Quizzes, Questions, and Answers
# -------------------------------------------------------------------
class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Quiz: {self.title}"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Q: {self.text[:50]}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"A: {self.text[:50]}"

# -------------------------------------------------------------------
# Course Reviews and Ratings
# -------------------------------------------------------------------
class CourseReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # rating on a 1-5 scale
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} ({self.rating}/5)"

# -------------------------------------------------------------------
# Enrollment and Progress Tracking
# -------------------------------------------------------------------
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)  # completion percentage (0.0 - 100.0)
    agreement_signed = models.BooleanField(default=False)  # T&C agreement
    mentor_verified = models.BooleanField(default=False)     # mentor verification

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"

# -------------------------------------------------------------------
# Certificates awarded upon course completion
# -------------------------------------------------------------------
class Certificate(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name='certificate')
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Certificate for {self.enrollment.user.username}"

# -------------------------------------------------------------------
# Live Sessions / Webinars for user engagement
# -------------------------------------------------------------------
class LiveSession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='live_sessions')
    title = models.CharField(max_length=200)
    scheduled_time = models.DateTimeField()
    webinar_link = models.URLField()
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='hosted_sessions')

    def __str__(self):
        return f"{self.course.title} - {self.title}"

# -------------------------------------------------------------------
# User Activity Logs for Analytics & Reporting
# -------------------------------------------------------------------
class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity}"
