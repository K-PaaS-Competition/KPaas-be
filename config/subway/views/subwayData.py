from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from subway.models import Subway


class SubwayData(APIView):
    def get(self, request, *args, **kwargs):
        try:
            stationName = request.GET["station"]
            print(stationName)
            subway = Subway.objects.filter(name=stationName).values()
        except KeyError:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "KeyError",
                }
            )
        return Response(subway)


class SubwayDataAll(APIView):
    def get(self, request, *args, **kwargs):
        subway = Subway.objects.all().values()
        return Response(subway)
