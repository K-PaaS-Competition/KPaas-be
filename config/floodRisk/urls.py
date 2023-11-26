from django.urls import path
from .views import LoadFloodData
from .views import FloodRiskByCityName
from .views import FloodRiskByCbc

app_name = "floodRisk"

urlpatterns = [
    # data/loadFloodRisk/
    path("load/", LoadFloodData.as_view()),
    # data/getFloodRisk/
    path("get/", FloodRiskByCityName.as_view()),
    path("getByCbc/", FloodRiskByCbc.as_view()),
]
