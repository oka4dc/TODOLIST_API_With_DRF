from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from API_App.models import items
from django.contrib.auth.models import User
from rest_framework import serializers

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=items
        fields=('FirstName', 'LastName', 'created')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
