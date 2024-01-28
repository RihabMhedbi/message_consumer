"""Consumer app models"""
from django.db import models


class TaskResult(models.Model):
    """Model to store information about Celery task results."""
    task_id = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    webhook_url = models.CharField(max_length=255)

    def __str__(self):
        return f'TaskResult: task_id={self.task_id},' \
               f' result={self.result}, webhook_url={self.webhook_url}'
