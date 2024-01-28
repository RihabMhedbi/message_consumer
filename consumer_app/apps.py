from django.apps import AppConfig


class ConsumerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consumer_app'

    def ready(self):
        import consumer_app.signals