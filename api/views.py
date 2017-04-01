from fiscalizaMapa.models import Incidente

from .serializers import IncidenteSerializer, LocationGeoSerializer
from rest_framework import viewsets, generics

# Create your views here.

class IncidenteViewSet(viewsets.ModelViewSet):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

class LocationList(viewsets.ModelViewSet):
    model = Incidente
    serializer_class = LocationGeoSerializer
    queryset = Incidente.objects.all()


