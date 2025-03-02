# courses/api/urls.py

from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet, ModuleViewSet, LessonViewSet, QuizViewSet,
    QuestionViewSet, AnswerViewSet, CourseReviewViewSet,
    EnrollmentViewSet, CertificateViewSet, LiveSessionViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'reviews', CourseReviewViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'livesessions', LiveSessionViewSet)

urlpatterns = router.urls
