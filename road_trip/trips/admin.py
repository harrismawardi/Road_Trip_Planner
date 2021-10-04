from django.contrib import admin
from .models import Pin, Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'access_token', 'owner_id')


class PinAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 'name', 'category', 'x_coordinates', 'y_coordinates', 'notes')

# Register your models here.
admin.site.register(Pin, PinAdmin)
admin.site.register(Trip, TripAdmin)