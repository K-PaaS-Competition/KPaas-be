from django.urls import path
from .views import LoadFloodData
from .views import FloodRiskByCityName

app_name = "data"

urlpatterns = [
    # data/loadFloodRisk/
    path("loadFloodRisk/", LoadFloodData.as_view()),
    # data/getFloodRisk/
    path("getFloodRisk/", FloodRiskByCityName.as_view()),
]
