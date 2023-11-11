from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from django.shortcuts import get_object_or_404
from rest_framework import status, generics

from back.models import MeasureSerializer, Measure, Patient, PatientSerializer

import json


# @csrf_exempt
# @api_view(['POST'])
# def save_measure(request):
#     measure = MeasureSerializer(data=request.data)
#
#     print(measure)
#     print(measure.is_valid())
#
#     if measure.is_valid():
#         measure.save()
#
#     return Response(measure.data)

# @api_view(['GET'])
# def get_measures(request):
#     measures = Measure.objects.all()
#     serializer = MeasureSerializer(measures, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def delete_measure(request, pk):
#     measure = get_object_or_404(Measure, pk=pk)
#     measure.delete()
#     return Response(status=status.HTTP_202_ACCEPTED)


class MeasuresView(generics.GenericAPIView):
    def get(self, request):
        measures = Measure.objects.all()
        serializer = MeasureSerializer(measures, many=True)
        return Response(serializer.data)

    def post(self, request):
        measure = MeasureSerializer(data=request.data)
        if measure.is_valid():
            measure.save()

        return Response(measure.data)


class MeasureDetailView(generics.GenericAPIView):
    def get(self, request, pk):
        measure = Measure.objects.get(pk=pk)
        serializer = MeasureSerializer(measure)
        return Response(serializer.data)

    # def patch(self, request, pk):
    #     note = self.get_note(pk)
    #     if note == None:
    #         return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = self.serializer_class(
    #         note, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.validated_data['updatedAt'] = datetime.now()
    #         serializer.save()
    #         return Response({"status": "success", "data": {"note": serializer.data}})
    #     return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        measure = get_object_or_404(Measure, pk=pk)
        measure.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class PatientsView(generics.GenericAPIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        patient = PatientSerializer(data=request.data)
        if patient.is_valid():
            patient.save()

        return Response(patient.data)


class PatientDetailView(generics.GenericAPIView):
    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def delete(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        patient.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
