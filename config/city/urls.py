from django.urls import path
from city.views import CityData

urlpatterns = [
    path("get", CityData.as_view()),
]
