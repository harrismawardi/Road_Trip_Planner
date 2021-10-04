from django.db import models
from users.models import User

# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    access_token = models.CharField(max_length=500, default=None)
    owner_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Pin(models.Model):
    trip_id = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    x_coordinates = models.FloatField()
    y_coordinates = models.FloatField()
    notes = models.CharField(max_length = 500)

    def __str__(self):
        return self.name
    