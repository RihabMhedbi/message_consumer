import base64
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import TaskResult


class ConsumerAPITests(TestCase):
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client = APIClient()
        self.client.force_login(self.user)

    @patch('consumer_app.tasks.process_message_data.delay')
    def test_message_processing_view(self, mock_process_message):
        # Mock the Celery task to return a task ID
        mock_task_id = 'fake-task-id'
        mock_process_message.return_value = mock_task_id

        # Define the data to be sent in the request body
        data = {'text': 'Test message', 'webhook_url': 'https://example.com/webhook'}

        # Make a POST request to the message processing view
        url = reverse('process_message')
        response = self.client.post(url, data, format='json')

        # Check if the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the task ID is returned in the response
        self.assertEqual(response.data['task_id'], mock_task_id)

    def test_result_endpoint(self):
        TaskResult.objects.create(task_id='776bc5d4-0182-4f85-a566-78c7adf5e29a', result='Processed result')
        url = f'/api/task_result/'
        basic_auth = 'Basic ' + base64.b64encode(f"{self.username}:{self.password}".encode()).decode('utf-8')
        response = self.client.get(url, HTTP_AUTHORIZATION=basic_auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['result'], 'Processed result')
