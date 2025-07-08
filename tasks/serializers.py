"""
Serializers for the tasks app.
Equivalent to Pydantic models in the original FastAPI implementation.
"""

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model, equivalent to TaskCreate and TaskUpdate in FastAPI."""
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class TaskCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating tasks, equivalent to TaskCreate Pydantic model."""
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        extra_kwargs = {
            'status': {'default': False}
        }


class TaskUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating tasks, equivalent to TaskUpdate Pydantic model."""
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
            'status': {'required': False}
        }


class TaskAnalyzeRequestSerializer(serializers.Serializer):
    """Serializer for task analysis requests, equivalent to TaskAnalyzeRequest Pydantic model."""
    description = serializers.CharField()


class TaskAnalyzeResponseSerializer(serializers.Serializer):
    """Serializer for task analysis responses."""
    category = serializers.CharField()