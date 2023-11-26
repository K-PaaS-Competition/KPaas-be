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
                city = City.objects.filter(name=cityName)
                if not city.exists():
                    City.objects.create(name=cityName)
                    city = City.objects.filter(name=cityName)
                # 강수량 정보 추가
                existData = FloodRisk.objects.filter(
                    gidChar=gidChar, gidCode1=gidCode1, gidCode2=gidCode2
                )
                if existData.exists():
                    # existData.update(
                    #     city=city.first(),
                    #     location=data["SGG_NM"],
                    #     gidChar=gidChar,
                    #     gidCode1=gidCode1,
                    #     gidCode2=gidCode2,
                    #     depth10Risk=data["DEPTH_10"],
                    #     depth20Risk=data["DEPTH_20"],
                    #     depth50Risk=data["DEPTH_50"],
                    # )
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
        # if not city:
        #     message = "해당하는 도시가 없습니다."
        #     return self.responseCode(400, message)
        # for i in range(len(floodData)):
        #     try:
        #         data = floodData.loc[i]
        #         gidChar = data["GID"][:2]
        #         gidCode1 = data["GID"][2:4]
        #         gidCode2 = data["GID"][4:]
        #         cityName = data["SD_NM"]
        #         if cityName == "서울":
        #             cnt += 1
        #         if gidChar != "다사":
        #             continue
        #         existData = FloodRisk.objects.filter(
        #             gidChar=gidChar, gidCode1=gidCode1, gidCode2=gidCode2
        #         )
        #         if existData.exists():
        #             existData.update(
        #                 city=city,
        #                 location=data["SGG_NM"],
        #                 gidChar=gidChar,
        #                 gidCode1=gidCode1,
        #                 gidCode2=gidCode2,
        #                 depth10Risk=data["DEPTH_10"],
        #                 depth20Risk=data["DEPTH_20"],
        #                 depth50Risk=data["DEPTH_50"],
        #             )
        #             continue
        #         floodRisk = FloodRisk(
        #             city=city,
        #             location=data["SGG_NM"],
        #             gidChar=gidChar,
        #             gidCode1=gidCode1,
        #             gidCode2=gidCode2,
        #             depth10Risk=data["DEPTH_10"],
        #             depth20Risk=data["DEPTH_20"],
        #             depth50Risk=data["DEPTH_50"],
        #         )
        #         floodRisk.save()
        #         added += 1
        #     except:
        #         failed += 1
        #         message = "DB에 데이터를 넣는 중 오류 발생"
        #         continue
        return Response(
            {
                "status": 200,
                "message": message,
                "added": added,
                "failed": failed,
                "cnt": cnt,
            }
        )
