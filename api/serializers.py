from rest_framework import serializers
from fiscalizaMapa.models import Incidente

from rest_framework_gis.serializers import GeoFeatureModelSerializer

class IncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidente
        fields = ('assunto',
                  'localizacao',)

class LocationGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Incidente
        geo_field = 'localizacao'
        fields = ('id', 'assunto')
