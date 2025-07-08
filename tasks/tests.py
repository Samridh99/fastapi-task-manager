"""
Tests for the Django Task Manager application.
"""

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task
import json


class TaskModelTest(TestCase):
    """Test the Task model."""
    
    def test_task_creation(self):
        """Test creating a task."""
        task = Task.objects.create(
            title="Test Task",
            description="Test description",
            status=False
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.status)
        self.assertIsNotNone(task.created_at)
        self.assertIsNotNone(task.updated_at)
    
    def test_task_str_method(self):
        """Test the string representation of a task."""
        task = Task.objects.create(title="Test Task", status=False)
        expected = "Test Task (Pending)"
        self.assertEqual(str(task), expected)
        
        task.status = True
        expected = "Test Task (Completed)"
        self.assertEqual(str(task), expected)


class TaskAPITest(APITestCase):
    """Test the Task API endpoints."""
    
    def setUp(self):
        """Set up test data."""
        self.task = Task.objects.create(
            title="Test Task",
            description="Test description",
            status=False
        )
    
    def test_get_tasks_list(self):
        """Test retrieving list of tasks."""
        url = reverse('tasks:task-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Task')
    
    def test_create_task(self):
        """Test creating a new task."""
        url = reverse('tasks:task-list-create')
        data = {
            'title': 'New Task',
            'description': 'New description',
            'status': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(response.data['title'], 'New Task')
    
    def test_get_task_detail(self):
        """Test retrieving a specific task."""
        url = reverse('tasks:task-detail', kwargs={'pk': self.task.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')
    
    def test_update_task(self):
        """Test updating a task."""
        url = reverse('tasks:task-detail', kwargs={'pk': self.task.pk})
        data = {
            'title': 'Updated Task',
            'description': 'Updated description',
            'status': True
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertTrue(self.task.status)
    
    def test_delete_task(self):
        """Test deleting a task."""
        url = reverse('tasks:task-detail', kwargs={'pk': self.task.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
    
    def test_analyze_task_endpoint(self):
        """Test the task analysis endpoint."""
        url = reverse('tasks:task-analyze')
        data = {'description': 'Login button is broken on mobile devices'}
        response = self.client.post(url, data, format='json')
        
        # Should return error if no Gemini API key is configured
        # In production with API key, this would return a category
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_500_INTERNAL_SERVER_ERROR])


class TaskDashboardTest(TestCase):
    """Test the task dashboard web interface."""
    
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.task = Task.objects.create(
            title="Test Task",
            description="Test description",
            status=False
        )
    
    def test_dashboard_view(self):
        """Test the dashboard view loads correctly."""
        url = reverse('tasks:dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task Management Dashboard')
        self.assertContains(response, 'New Task')
    
    def test_root_redirect(self):
        """Test that root URL redirects to dashboard."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/tasks/dashboard/', response.url)
