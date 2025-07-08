"""
URL routing for the tasks app.
Equivalent to the FastAPI route definitions.
"""

from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # Dashboard HTML interface
    path('dashboard/', views.TaskDashboardView.as_view(), name='dashboard'),
    
    # Task CRUD API endpoints
    path('', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    
    # Task analysis endpoint
    path('analyze/', views.analyze_task, name='task-analyze'),
]