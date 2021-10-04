from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TripSerializer, PinSerializer
from .models import Trip, Pin

# Create your views here.
class TripView(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

class PinView(viewsets.ModelViewSet):
    serializer_class = PinSerializer
    queryset = Pin.objects.all()