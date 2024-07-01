from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer

class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return SensorDetailSerializer
        return SensorSerializer

class MeasurementCreateAPIView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

@api_view(['POST'])
def add_measurement(request, pk):
    sensor = Sensor.objects.get(pk=pk)
    data = request.data
    data['sensor'] = sensor.id
    serializer = MeasurementSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
