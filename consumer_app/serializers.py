"""Consumer app serializers."""
from rest_framework import serializers
from consumer_app.models import TaskResult


class TaskResultSerializer(serializers.ModelSerializer):
    """Serializer for the TaskResult model."""
    class Meta:
        model = TaskResult
        fields = ['task_id', 'result', 'webhook_url']
