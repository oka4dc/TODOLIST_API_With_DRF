from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class items(models.Model):
    FirstName=models.CharField(max_length=200)
    LastName=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)