from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementCreateAPIView, add_measurement

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view(), name='sensor-retrieve-update'),
    path('measurements/', MeasurementCreateAPIView.as_view(), name='measurement-create'),
    path('sensors/<int:pk>/add_measurement/', add_measurement, name='add-measurement'),
]
