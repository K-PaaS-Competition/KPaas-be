from django.urls import path
from city.views import *

urlpatterns = [
    path("get/", CityData.as_view()),
    path("load/", LoadData.as_view()),
]
