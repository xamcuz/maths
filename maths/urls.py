from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.home.urls')),
    path('courses/', include('apps.courses.urls')),
    path('games/', include('apps.games.urls')),
    path('admin/', admin.site.urls),
]
