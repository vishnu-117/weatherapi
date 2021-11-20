from django.urls import path
from .views import WeatherView

urlpatterns = [
    path('weather/', WeatherView.as_view()),
    path('weather/<int:pk>/', WeatherView.as_view()),
]
