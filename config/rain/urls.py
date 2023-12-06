from django.urls import path
from rain.views import RainData
from rain.views import Test

urlpatterns = [
    path("get/", RainData.as_view()),
    path("test/", RainData.as_view()),
]
