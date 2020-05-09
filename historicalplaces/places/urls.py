from  django.conf.urls import url, include
from places.views import PlacesList, RatesList

urlpatterns = [
    url(r'^places/$', PlacesList.as_view(), name='places_list'),
    url(r'^rates/$', RatesList.as_view(), name='rates_list'),
    url(r'^place/(?P<pk>[0-9]+)/$', RatesList.as_view(), name='place_detail'),
]