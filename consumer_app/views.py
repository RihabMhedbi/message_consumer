from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from .models import TaskResult
from .serializers import TaskResultSerializer
from .tasks import process_message_data


@api_view(['POST'])
def process_message(request):
    message_data = request.data.get('message')
    webhook_url = request.data.get('webhook_url')

    task_id = process_message_data.delay(message_data, webhook_url)
    return Response({'task_id': str(task_id)})


class TaskResultViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
