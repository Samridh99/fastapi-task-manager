"""
Django REST API views for tasks.
Equivalent to the FastAPI endpoints in main.py.
"""

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from .models import Task
from .serializers import (
    TaskSerializer, 
    TaskCreateSerializer, 
    TaskUpdateSerializer,
    TaskAnalyzeRequestSerializer,
    TaskAnalyzeResponseSerializer
)
from analysis.services import get_analyzer


class TaskDashboardView(TemplateView):
    """Dashboard view for tasks management with HTML interface."""
    template_name = 'task_list.html'


class TaskListCreateView(generics.ListCreateAPIView):
    """
    GET /tasks/ - List all tasks
    POST /tasks/ - Create a new task
    """
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /tasks/{id}/ - Retrieve a specific task
    PUT /tasks/{id}/ - Update a specific task
    DELETE /tasks/{id}/ - Delete a specific task
    """
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskUpdateSerializer
        return TaskSerializer


@api_view(['POST'])
def analyze_task(request):
    """
    POST /tasks/analyze/ - Analyze a task description and categorize it
    Equivalent to the analyze_task FastAPI endpoint.
    """
    serializer = TaskAnalyzeRequestSerializer(data=request.data)
    if serializer.is_valid():
        description = serializer.validated_data['description']
        
        try:
            analyzer = get_analyzer()
            category = analyzer.analyze(description)
            
            response_serializer = TaskAnalyzeResponseSerializer({'category': category})
            return Response(response_serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'detail': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
