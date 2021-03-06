# Generated by Django 3.1 on 2021-02-27 22:53

from django.db import migrations

def create_sensors(apps, schema_editor):
    ids = ["uuid0129", "uuid0130", "uuid0100"]
    Sensor = apps.get_model('tomatoes', 'Sensor')
    sensors = [Sensor(id=id) for id in ids]
    for sensor in sensors:
        sensor.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tomatoes', '0002_auto_20210227_1628'),
    ]

    operations = [
        migrations.RunPython(create_sensors),
    ]
