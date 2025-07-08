from django.db import models


class Task(models.Model):
    """
    Task model equivalent to the SQLAlchemy Task model.
    Stores task information with title, description, and completion status.
    """
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)  # False = Pending, True = Completed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({'Completed' if self.status else 'Pending'})"
