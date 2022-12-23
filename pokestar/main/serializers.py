from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Cities

class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cities
        fields = "__all__"

class CitiesGeoJSONSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Cities
        geo_field = 'geometry'
        fields = "__all__"
