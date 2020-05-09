from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from places.models import Place, Rate
from places.serializers import PlaceSerializer, RateSerializer


class PlacesList(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class RatesList(ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class PlaceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = PlaceSerializer
