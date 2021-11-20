from .models import Weather
from .serializers import WeatherSerializer
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from .weather import weatherdata 


class WeatherView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def create(self, request, *args, **kwargs):
        data = weatherdata()
        serialized_obj = WeatherSerializer(data=data, context={'data': data})
        if serialized_obj.is_valid():
            instance = serialized_obj.save()
        else:
            return Response(serialized_obj.errors, status=400)
        qs = WeatherSerializer(self.get_queryset(), many=True)
        return Response(data=qs.data, status=200)

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.http_method_not_allowed(request)
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
