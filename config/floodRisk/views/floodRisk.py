from floodRisk.models import FloodRisk
from floodRisk.serializers import FloodDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from city.models import City
from floodRisk.models import FloodRisk


# 적절한 요청을 받으면 침수 위험도 데이터를 조회해주는 라우터
class FloodRiskByCityName(APIView):
    def get(self, request):
        try:
            cityName = request.GET["city"]
            city = City.objects.filter(name=cityName)
            if not city.exists():
                return Response(
                    {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": "해당하는 지역의 정보가 없습니다",
                    }
                )
            floodRisk = list(FloodRisk.objects.filter(city=city.first()).values())
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "length": len(floodRisk),
                    "data": floodRisk,
                }
            )
        except KeyError:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "city 데이터를 넘겨주세요",
                }
            )


class FloodRiskByCbc(APIView):
    def get(self, request, *args, **kwargs):
        try:
            gidChar = request.GET["gidChar"]
            gidCode1 = request.GET["gidCode1"]
            gidCode2 = request.GET["gidCode2"]
            floodRisk = FloodRisk.objects.filter(
                gidChar=gidChar, gidCode1=gidCode1, gidCode2=gidCode2
            ).values()
            return Response(floodRisk)
        except KeyError:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "gidChar, gidCode1, gidCode2 데이터를 넘겨주세요",
                }
            )
        except:
            return Response(
                {
                    "staus": status.HTTP_400_BAD_REQUEST,
                    "message": "other Error",
                }
            )
