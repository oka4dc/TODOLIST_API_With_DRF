from pickle import GET
from rest_framework.response import Response
from rest_framework.decorators import api_view
from API_App.models import items
from My_API.serializers import ItemsSerializer

# accounts/views.py

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def GetData(request):
    #person = ['Dennis', 'Okafor', 23]
    #person = {"Name": "Dennis", "Age": 24}
    item=items.objects.all()
    serializer=ItemsSerializer(item, many=True)
    return Response(serializer.data)