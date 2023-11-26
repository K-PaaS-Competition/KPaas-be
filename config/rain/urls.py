from django.urls import path
from rain.views import RainData

urlpatterns = [
    path("get/", RainData.as_view()),
    path("load/", RainData.as_view()),
]
