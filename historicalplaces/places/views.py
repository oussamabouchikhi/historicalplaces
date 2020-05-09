from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from places.models import Place, Rate
from places.serializers import PlaceSerializer, RateSerializer


class PlacesViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class RatesViewSet(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

