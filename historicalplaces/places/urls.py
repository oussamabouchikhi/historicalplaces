from  django.conf.urls import url, include
from places.views import PlacesList

urlpatterns = [
    url(r'^places/$', PlacesList.as_view(), name='places_list'),
]