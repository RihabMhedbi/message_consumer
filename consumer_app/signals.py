import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from consumer_app.models import TaskResult
from message_consumer.settings import PRODUCER_URL, PRODUCER_API_KEY


@receiver([post_save], sender=TaskResult)
def send_result_to_producer(sender, instance, **kwargs):
    webhook_url = instance.webhook_url
    headers = {"Authorization": f"Api-Key {PRODUCER_API_KEY}"}
    if webhook_url:
        result_data = {'result': instance.result}
        requests.post(f"{PRODUCER_URL}{webhook_url}", json=result_data, headers=headers)
