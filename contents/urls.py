from django.urls import path
from .views import lesson_contents

urlpatterns = [
    path('lesson/<int:lesson_id>/', lesson_contents, name='lesson-contents'),
]
