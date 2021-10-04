from rest_framework import serializers
from .models import Pin, Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Trip
        fields = ('name', 'description', 'access_token', 'owner_id')

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = ('trip_id', 'name', 'category', 'x_coordinates', 'y_coordinates', 'notes')