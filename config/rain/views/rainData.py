from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
import requests
import os, ast
import random

load_dotenv()


class RainData(APIView):
    def get(self, request, *args, **kwargs):
        CumulativeTime = int(request.GET["Cumulative_time"])  # 누적 시간
        dataSize = 46 * (CumulativeTime // 10)  # 요청할 데이터 수
        # 요청 데이터 수 조정
        if dataSize < 1:
            dataSize = 1
        elif dataSize > 1000:
            dataSize = 966
            CumulativeTime = 21
        apiKey = os.environ.get("RAIN_APIKEY")
        result = []
        try:
            result = requests.get(
                f"http://openAPI.seoul.go.kr:8088/{apiKey}/json/ListRainfallService/1/{dataSize}/",
            )
            result = result.text
            result = ast.literal_eval(result)
            result = result["ListRainfallService"]["row"]
        except:
            return Response(status.HTTP_400_BAD_REQUEST)
        # 구청 이름 집합 만들기
        guNameSet = set()
        rainFallDict = {}
        for item in result:
            guName = item["GU_NAME"]
            if not guName in guNameSet:
                guNameSet.add(guName)
        # 구청별로 강수량 데이터 정리
        for guName in guNameSet:
            try:
                dataSet = [
                    float(item["RAINFALL10"])
                    for item in result
                    if item["GU_NAME"] == guName
                ]
                length = len(dataSet) // (CumulativeTime // 10)
                rainFall = sum(dataSet) / length
                rainFallDict[guName] = {"rainFall": rainFall}
            except ZeroDivisionError:
                return Response(status.HTTP_400_BAD_REQUEST)
            except:
                return Response(status.HTTP_400_BAD_REQUEST)
        return Response(rainFallDict)
