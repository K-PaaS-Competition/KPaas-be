from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from django.conf import settings
from city.models import SubRegion, City
import os


class LoadData(APIView):
    def post(self, request, *args, **kwargs):
        filePath = settings.STATICFILES_DIRS[2] / "dbf" / "cityInfoDetail.xlsx"
        table = pd.read_excel(filePath, engine="openpyxl")
        table = table.fillna(value=0)
        table = table.loc[
            (table["읍면동/구"] == 0) & (table["읍/면/리/동"] == 0) & (table["리"] == 0)
        ]
        print(table)
        table = table.reset_index()
        print(table)
        cityName = table.loc[0]["시도"]
        city = City.objects.filter(name=cityName).first()
        added = 0
        for i in range(len(table)):
            data = table.loc[i]
            print(data)
            prev = SubRegion.objects.filter(name=data["시군구"])
            if prev.exists():
                prev.update(name=data["시군구"], lat=data["위도"], lng=data["경도"], city=city)
            else:
                subRegion = SubRegion(
                    name=data["시군구"], lat=data["위도"], lng=data["경도"], city=city
                )
                subRegion.save()
                added += 1
        return Response({added})
