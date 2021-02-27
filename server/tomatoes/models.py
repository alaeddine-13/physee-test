from django.db import models
import uuid


class TomatoPlant(models.Model):
    name = models.CharField(max_length=30)


class Production(models.Model):
    tomato_plant = models.ForeignKey(TomatoPlant, on_delete=models.CASCADE)
    harvest_date  = models.DateTimeField()
    number_of_plants = models.IntegerField()
    weight_in_ton = models.IntegerField()


class Sensor(models.Model):
    id = models.CharField(primary_key=True, max_length = 20, default=uuid.uuid1, editable=True)

class SensorData(models.Model):
    TARGETS = (
        ("environment", "Environment"),
        ("soil", "Soil"),
    )
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    time  = models.DateTimeField()
    target = models.CharField(max_length=20, choices=TARGETS)
    data = models.JSONField()
