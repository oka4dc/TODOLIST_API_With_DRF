# todoapp/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from API_App.models import Todo
from API_App.serializers import TodoSerializer
from django.http import Http404

class TodoListCreate(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of todos",
        responses={200: TodoSerializer(many=True)},
    )
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new todo",
        request_body=TodoSerializer,
        responses={201: TodoSerializer},
        examples={
            "application/json": {
                "title": "Sample Todo",
                "description": "This is a sample description.",
                "completed": False
            }
        }
    )
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a single todo",
        responses={200: TodoSerializer},
    )
    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update a todo",
        request_body=TodoSerializer,
        responses={200: TodoSerializer},
        examples={
            "application/json": {
                "title": "Updated Todo",
                "description": "This is an updated description.",
                "completed": True
            }
        }
    )
    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a todo",
        responses={204: 'No Content'},
    )
    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

