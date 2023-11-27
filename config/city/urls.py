from django.urls import path
from city.views import *

urlpatterns = [
    path("get/", CityData.as_view()),
    path("getAll/", CityDataAll.as_view()),
    path("load/", LoadData.as_view()),
    path("subRegion/all/", SubRegionData.as_view()),
    path("subRegion/city/", SubRegionDataByCity.as_view()),
]
