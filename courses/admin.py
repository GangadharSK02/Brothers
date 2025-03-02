from django.contrib import admin
from .models import (
    Course, Module, Lesson, Quiz, Question, Answer,
    CourseLevel, CourseCategory, CourseReview, Enrollment, Certificate,
    LiveSession, UserActivityLog
)

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(CourseLevel)
admin.site.register(CourseCategory)
admin.site.register(CourseReview)
admin.site.register(Enrollment)
admin.site.register(Certificate)
admin.site.register(LiveSession)
admin.site.register(UserActivityLog)
