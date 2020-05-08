from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from places.models import Place
from places.serializers import PlaceSerializer


class PlacesList(APIView):
    def get(self, request, format=None):
        # get all places from database
        places = Place.object.all()
        # many=True means we gonna send a list of data to serializer
        serializer = PlaceSerializer(places, many=True)
        # return response data as json
        return Response(serializer.data)