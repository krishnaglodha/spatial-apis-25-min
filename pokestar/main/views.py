from django.shortcuts import render
from .models import Cities
from .serializers import CitiesSerializer, CitiesGeoJSONSerializer
from rest_framework import viewsets
from rest_framework_gis.filters import InBBoxFilter,TMSTileFilter,DistanceToPointFilter

class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


def home(request):
    allcities = Cities.objects.all()
    contenxt = {
        'allcities':allcities
    }
    return render(request, 'home.html',contenxt)


class CitiesGeoJSONViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesGeoJSONSerializer 


class CitiesInBBOX(viewsets.ModelViewSet):

    queryset = Cities.objects.all()
    serializer_class = CitiesGeoJSONSerializer
    bbox_filter_field = 'geometry'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True # Optional

class CitiesInTMS(viewsets.ModelViewSet):

    queryset = Cities.objects.all()
    serializer_class = CitiesGeoJSONSerializer
    bbox_filter_field = 'geometry'
    filter_backends = (TMSTileFilter,)
    bbox_filter_include_overlapping = True # Optional
