from django.urls import path
from .views import loadFloodRisk
from .views import getFloodRisk

app_name = "data"

urlpatterns = [
    # data/loadFloodRisk/
    path("loadFloodRisk/", loadFloodRisk),
    # data/getFloodRisk/
    path("getFloodRisk/", getFloodRisk),
]
