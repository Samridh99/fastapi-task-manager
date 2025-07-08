"""
URL configuration for task_manager_django project.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls', namespace='api-tasks')),
    path('tasks/', include('tasks.urls')),
    path('', lambda request: redirect('/tasks/dashboard/')),  # Redirect root to dashboard
]
