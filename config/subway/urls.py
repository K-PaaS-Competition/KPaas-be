from django.urls import path
from .views import LoadSubwayData

app_name = "subway"

urlpatterns = [
    path("loadData/", LoadSubwayData.as_view()),
]
