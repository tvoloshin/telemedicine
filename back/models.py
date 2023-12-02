from django.core import serializers
from django.db import models

from rest_framework import serializers


class Patient(models.Model):
    name = models.TextField()


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class Measure(models.Model):
    sys = models.IntegerField()
    dia = models.IntegerField()
    pr = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        # fields = '__all__'
        fields = ['id', 'sys', 'dia', 'pr']