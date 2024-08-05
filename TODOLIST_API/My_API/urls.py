from django.urls import path
from . import views
from .views import UserList, UserDetail

urlpatterns = [
    path('', views.GetData),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

]