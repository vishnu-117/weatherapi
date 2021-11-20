from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        exclude = []

    def create(self, validated_data):
        weather_data = self.context['data']['data']

        for data in weather_data:
            Weather.objects.create(**data)
        return ''
