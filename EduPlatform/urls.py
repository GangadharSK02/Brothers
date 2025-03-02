from django.contrib import admin
from django.urls import path, include
import debug_toolbar 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('contents/', include('contents.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # API endpoints
    path('api/courses/', include('courses.api.urls')),
    path('api/contents/', include('contents.api.urls')),
    path('api/users/', include('users.api.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
