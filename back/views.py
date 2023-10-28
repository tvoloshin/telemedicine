from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from back.models import MeasureSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def save_measure(request):
    measure = MeasureSerializer(data=request.data)

    print(measure)
    print(measure.is_valid())

    if measure.is_valid():
        measure.save()

    return Response(measure.data)
