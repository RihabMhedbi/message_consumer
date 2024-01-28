"""Consumer app tasks."""
from celery import shared_task
from .models import TaskResult


@shared_task
def process_message_data(message_data, webhook_url):
    """Process message data asynchronously.

        Args:
            message_data: Message data
            webhook_url: Webhook URL

        Returns:
            ID of the created TaskResult instance.
        """
    processed_data = message_data[::-1]
    result = TaskResult.objects.create(result=processed_data, task_id=process_message_data.request.id,
                                       webhook_url=webhook_url)
    return result.id
