from django.core import serializers
from django.db import models

from rest_framework import serializers


class Measure(models.Model):
    patient_id = models.IntegerField()
    sys = models.IntegerField()
    dia = models.IntegerField()
    pr = models.IntegerField()


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = '__all__'