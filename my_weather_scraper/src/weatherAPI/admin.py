from django.contrib import admin
from .models import *


class WeatherAdmin(admin.ModelAdmin):
    list_display = ['id', 'day', 'description', 'temperature']
    search_fields = ['id', 'day', 'description', 'temperature']

admin.site.register(Weather, WeatherAdmin)