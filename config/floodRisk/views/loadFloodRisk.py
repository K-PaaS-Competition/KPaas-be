from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from floodRisk.models import FloodRisk
import pandas as pd
from django.conf import settings
from city.models import City


class LoadFloodData(APIView):
    def responseCode(self, status, message):
        return Response(
            {
                "status": status,
                "message": message,
            }
        )

    def post(self, request):
        filePath = settings.STATICFILES_DIRS[0] / "csv" / "floodData2023.csv"
        added = 0
        failed = 0
        cnt = 0
        try:
            floodData = pd.read_csv(filePath, encoding="cp949")
            if floodData.empty:
                message = "csv is empty"
                return self.responseCode(400, message)
            for idx in range(len(floodData)):
                print(idx)
                data = floodData.loc[idx]
                cityName = data["SD_NM"]
                gidChar = data["GID"][:2]
                gidCode1 = data["GID"][2:4]
                gidCode2 = data["GID"][4:]
                # 도시 정보 추가
                if not gidChar or not gidCode1 or not gidCode2:
                    continue
                city = City.objects.filter(name=cityName)
                if not city.exists():
                    continue
                # 강수량 정보 추가
                existData = FloodRisk.objects.filter(
                    gidChar=gidChar, gidCode1=gidCode1, gidCode2=gidCode2
                )
                if existData.exists():
                    continue
                FloodRisk.objects.create(
                    city=city.first(),
                    location=data["SGG_NM"],
                    gidChar=gidChar,
                    gidCode1=gidCode1,
                    gidCode2=gidCode2,
                    depth10Risk=data["DEPTH_10"],
                    depth20Risk=data["DEPTH_20"],
                    depth50Risk=data["DEPTH_50"],
                )
                added += 1
        except FileNotFoundError:
            message = "FileNotFoundError"
            return self.responseCode(400, message)
        return Response(
            {
                "status": 200,
                "message": message,
                "added": added,
                "failed": failed,
                "cnt": cnt,
            }
        )
