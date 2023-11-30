from django.urls import path
from .views import LoadSubwayData
from .views import SubwayData, SubwayDataAll

app_name = "subway"

urlpatterns = [
    path("loadData/", LoadSubwayData.as_view()),
    path("get/", SubwayData.as_view()),
    path("getAll/", SubwayDataAll.as_view()),
]
