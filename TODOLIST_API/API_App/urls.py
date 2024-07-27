# todoapp/urls.py

from django.urls import path
from API_App.views import TodoListCreate, TodoDetail

urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]
