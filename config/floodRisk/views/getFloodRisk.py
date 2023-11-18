from floodRisk.models import FloodRisk
from floodRisk.serializers import FloodDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 적절한 요청을 받으면 침수 위험도 데이터를 조회해주는 라우터
@api_view(["GET"])
def getFloodRisk(request):
    queryset = FloodRisk.objects.all()
    if request.GET.get("location"):
        print(request.GET.get("location"))
        location = request.GET.get("location")
        queryset = FloodRisk.objects.filter(location=location)
    # many : 중복된 데이터를 list로 받는다.
    serializer = FloodDataSerializer(queryset, many=True)
    return Response({"data": serializer.data})
