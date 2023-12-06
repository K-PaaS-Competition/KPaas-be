from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from city.models import SubRegion, City


class SubRegionData(APIView):
    # 전부 반환
    def get(self, request, *args, **kwargs):
        data = SubRegion.objects.all()
        return Response(data.values())


class SubRegionDataByCity(APIView):
    def get(self, request, *args, **kwargs):
        try:
            cityName = request.GET["city"]
            city = City.objects.filter(name=cityName)
            if city.exists():
                subRegion = SubRegion.objects.filter(city=city.first())
                print(subRegion)
                return Response(
                    {
                        "data": subRegion.values(),
                        "status": 200,
                    }
                )
            return Response(
                {
                    "data": None,
                    "message": "Data Not Exist",
                    "status": 400,
                }
            )
        except KeyError:
            return Response(
                {
                    "data": None,
                    "message": "KeyError",
                    "status": 400,
                }
            )
