from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo

class TodoTests(APITestCase):
    def setUp(self):
        self.todo1 = Todo.objects.create(title="Test Todo 1", description="Test Description 1", completed=False)
        self.todo2 = Todo.objects.create(title="Test Todo 2", description="Test Description 2", completed=False)
        print(self.todo2)

    def test_create_todo(self):
        url = reverse('todo-list-create')
        data = {'title': 'Test Todo 3', 'description': 'Test Description 3', 'completed': False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #print("object created test passed")
        self.assertEqual(Todo.objects.count(), 3)

    def test_get_todos(self):
        url = reverse('todo-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        #print("object GET test passed")

    def test_get_single_todo(self):
        url = reverse('todo-detail', args=[self.todo1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.todo1.title)

    def test_update_todo(self):
        url = reverse('todo-detail', args=[self.todo1.id])
        data = {'title': 'Updated Title', 'description': 'Updated Description', 'completed': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo1.refresh_from_db()
        self.assertEqual(self.todo1.title, 'Updated Title')

    def test_delete_todo(self):
        url = reverse('todo-detail', args=[self.todo1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 1)

