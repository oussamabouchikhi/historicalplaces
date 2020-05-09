from  django.conf.urls import url, include
from rest_framework import routers

from places.views import PlacesViewSet, RatesViewSet

router = routers.DefaultRouter()
router.register(r'places', PlacesViewSet)
router.register(r'rates', RatesViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]