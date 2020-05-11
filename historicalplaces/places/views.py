from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from places.models import Place, Rate
from places.serializers import PlaceSerializer, RateSerializer


class PlacesViewSet(ModelViewSet):
    # When adding permission_classes property default permissions from settings.py will be ignored
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class RatesViewSet(ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

