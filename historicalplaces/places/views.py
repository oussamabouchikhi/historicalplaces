from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from places.models import Place
from places.serializers import PlaceSerializer


class PlacesList(APIView):
    # Get all places
    def get(self, request, format=None):
        # get all places from database
        places = Place.objects.all()
        # many=True means we gonna send a list of data to serializer
        serializer = PlaceSerializer(places, many=True)
        # return response data as json
        return Response(serializer.data)

    # Create a new place
    def post(self, request, format=None):
        # send data from request to serializer
        serializer = PlaceSerializer(data=request.data)
        serializer.save() # save data
        # return response as json with status 201(created)
        return Response(serializer.data, status=status.HTTP_201_CREATED)