from django.urls import path

from consumer_app import views

urlpatterns = [
    path('process_message/', views.process_message, name="process_message")
]
