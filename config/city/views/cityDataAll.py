from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from city.models import City


class CityDataAll(APIView):
    def responseCode(self, status, message):
        return Response(
            {
                "status": status,
                "message": message,
            }
        )

    # 특정 도시 데이터 반환
    def get(self, request, *args, **kwargs):
        city = City.objects.all()
        return Response(
            {
                "status": 200,
                "data": city.values(),
            }
        )
