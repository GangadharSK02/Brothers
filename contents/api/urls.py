# contents/api/urls.py

from rest_framework.routers import DefaultRouter
from .views import TextContentViewSet, VideoContentViewSet, FileContentViewSet

router = DefaultRouter()
router.register(r'textcontents', TextContentViewSet)
router.register(r'videocontents', VideoContentViewSet)
router.register(r'filecontents', FileContentViewSet)

urlpatterns = router.urls
