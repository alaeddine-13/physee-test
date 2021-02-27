from rest_framework import  serializers
from .models import TomatoPlant, Production, SensorData
from rest_framework.settings import api_settings
from datetime import datetime

class TimestampToDateTimeField(serializers.DateTimeField):
    def to_internal_value(self, value):
        return datetime.fromtimestamp(int(int(value)/1000))

    def to_representation(self, value):
        return value.strftime("%s000")

class TomatoPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TomatoPlant
        fields = '__all__'

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'
    data = serializers.JSONField()
    time = TimestampToDateTimeField(help_text="timestamp value")
