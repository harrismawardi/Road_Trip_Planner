from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=30, default=None)
    email = models.EmailField(default=None) 