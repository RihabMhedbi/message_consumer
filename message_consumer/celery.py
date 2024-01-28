import os
from celery import Celery
from message_consumer import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'message_consumer.settings')
app = Celery('message_consumer')

app.conf_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
