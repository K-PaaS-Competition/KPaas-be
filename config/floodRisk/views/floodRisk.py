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
        cityName = request.GET["cityname"]
        if not cityName:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "cityName 데이터를 넘겨주세요",
                }
            )
        city = City.objects.filter(name=cityName).first()
        floodRisk = list(FloodRisk.objects.filter(city=city).values())
        serializer = FloodDataSerializer(data=floodRisk, many=True)
        if serializer.is_valid():
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "success",
                    "data": serializer.validated_data,
                }
            )
        else:
            print(serializer.errors)
        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "serializer가 유효하지 않습니다",
                "data": cityName,
            }
        )
