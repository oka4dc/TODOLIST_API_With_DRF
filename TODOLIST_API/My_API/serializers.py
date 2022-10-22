from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from API_App.models import items

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=items
        fields=('FirstName', 'LastName', 'created')