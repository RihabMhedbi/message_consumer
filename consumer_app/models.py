from django.db import models


class TaskResult(models.Model):
    task_id = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    webhook_url = models.CharField(max_length=255)
