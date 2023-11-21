from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import os, ast
from dotenv import load_dotenv
from city.serializers import CityNameSerializer
from city.models import City
from subway.models import Subway
import requests

load_dotenv()


class LoadSubwayData(APIView):
    def error400(self, message):
        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": message,
            }
        )

    def post(self, request, *args, **kwargs):
        # 도시 데이터 가져오기
        serializer = CityNameSerializer(data=request.data)
        cityName = None
        if serializer.is_valid():
            cityName = serializer.validated_data.get("name")
        city = City.objects.filter(name=cityName).first()
        if not city:
            return self.error400("해당 도시에 해당하는 데이터가 없습니다.")
        # api 요청을 보내서 지하철 데이터를 받아온다.
        data = None
        try:
            apiKey = os.environ.get("SUBWAY_APIKEY")
            data = requests.get(
                f"http://t-data.seoul.go.kr/apig/apiman-gateway/tapi/TaimsKsccDvSubwayStationGeom/1.0?apikey={apiKey}&startRow=1&rowCnt=1500"
            )
            data = ast.literal_eval(data.text)
        except:
            return self.error400("해당 데이터가 없습니다")
        # DB에 데이터 추가
        added = 0
        failed = 0
        try:
            for idx in range(len(data)):
                dt = data[idx]
                if Subway.objects.filter(id=dt["outStnNum"]).first():
                    continue
                subway = Subway(
                    id=dt["outStnNum"],
                    city=city,
                    name=dt["stnKrNm"],
                    line=dt["lineNm"],
                    lat=dt["convY"],
                    lng=dt["convX"],
                )
                subway.save()
                added += 1
        except:
            failed += 1
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "success",
                "added": added,
                "failed": failed,
            }
        )
