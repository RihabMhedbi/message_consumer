from django.urls import path, include
from rest_framework.routers import DefaultRouter

from consumer_app import views
from consumer_app.views import TaskResultViewSet

router = DefaultRouter()
router.register(r'task_result', TaskResultViewSet)

urlpatterns = [
    path('process_message/', views.process_message, name="process_message"),
    path('', include(router.urls), name='task_result_api')
]
