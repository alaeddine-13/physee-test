from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
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

class TomatoesPlantView(APIView):
    queryset = queryset = TomatoPlant.objects.all()
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request, *args, **kwargs):
        return Response({"tomatoes": self.queryset.all().values()}, template_name='tomatoes.html')


class ProductionCreateListView(generics.ListCreateAPIView):
    serializer_class = ProductionSerializer
    queryset = Production.objects.all()

class ProductionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductionSerializer
    queryset = Production.objects.all()

class ProductionsView(APIView):
    queryset = Production.objects.select_related("tomato_plant", "name", "number_of_plants")
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request, *args, **kwargs):
        return Response({"production": self.queryset.all().values()}, template_name='production.html')


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
        return Response({"environment": self.queryset.all().values()}, template_name='environment.html')


class SoilView(APIView):
    queryset = SensorData.objects.filter(target='soil')
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request, *args, **kwargs):
        return Response({"soil": self.queryset.all().values()}, template_name='soil.html')

