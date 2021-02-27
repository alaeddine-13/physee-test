from django.shortcuts import render
from rest_framework import generics
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
