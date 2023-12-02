from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from city.models import City
from city.serializers import CityDetailInfoSerializer


class CityData(APIView):
    def responseCode(self, status, message):
        return Response(
            {
                "status": status,
                "message": message,
            }
        )

    # 특정 도시 데이터 반환
    def get(self, request):
        name = request.GET["city"]
        # serializer 적용하려면 values로 가져와라
        data = None
        try:
            print(City.objects.filter().values)
            data = (City.objects.filter(name=name).values())[0]
        except:
            return self.responseCode(400, "orm으로 데이터 로드 실패")
        if not data:
            return self.responseCode(400, "데이터가 없습니다.")
        # serializer로 데이터 정제
        serializer = CityDetailInfoSerializer(data=data)
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
                "message": "fail to load data",
            }
        )
