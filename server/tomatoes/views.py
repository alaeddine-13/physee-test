from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from .models import (
    TomatoPlant,
    Production,
    SensorData,
)
from .serializers import (
    TomatoPlantSerializer,
    ProductionSerializer,
    SensorDataSerializer,
)

class TomatoPlantCreateListView(generics.ListCreateAPIView):
    serializer_class = TomatoPlantSerializer
    queryset = TomatoPlant.objects.all()

class TomatoPlantView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TomatoPlantSerializer
    queryset = TomatoPlant.objects.all()

class ProductionCreateListView(generics.ListCreateAPIView):
    serializer_class = ProductionSerializer
    queryset = Production.objects.all()

class ProductionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductionSerializer
    queryset = Production.objects.all()

class SensorDataCreateListView(generics.ListCreateAPIView):
    serializer_class = SensorDataSerializer
    queryset = SensorData.objects.all()

class SensorDataView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorDataSerializer
    queryset = SensorData.objects.all()

class EnvironmentView(APIView):
    queryset = SensorData.objects.filter(target='environment')
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request, *args, **kwargs):
        return Response(self.queryset.all(), template_name='environment.html')


class SoilView(APIView):
    queryset = SensorData.objects.filter(target='soil')
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request, *args, **kwargs):
        return Response(self.queryset.all(), template_name='soil.html')

