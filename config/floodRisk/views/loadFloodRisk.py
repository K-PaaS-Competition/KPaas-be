from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from floodRisk.models import FloodRisk
import pandas as pd
from django.conf import settings


@api_view(["GET"])
def loadFloodRisk(request):
    filePath = settings.STATICFILES_DIRS[0] / "csv" / "floodData.csv"
    try:
        floodData = pd.read_csv(filePath)
        added = 0
        for i in range(len(floodData)):
            data = floodData.loc[i]
            gidChar = data["GID"][:2]
            gidCode1 = data["GID"][2:4]
            gidCode2 = data["GID"][4:]
            if FloodRisk.objects.filter(
                gidChar=gidChar, gidCode1=gidCode1, gidCode2=gidCode2
            ):
                continue
            added += 1
            floodRisk = FloodRisk()
            floodRisk.location = data["SGG_NM"]
            floodRisk.gidChar = gidChar
            floodRisk.gidCode1 = gidCode1
            floodRisk.gidCode2 = gidCode2
            floodRisk.depth10Risk = data["DEPTH_10"]
            floodRisk.depth20Risk = data["DEPTH_20"]
            floodRisk.depth50Risk = data["DEPTH_50"]
            floodRisk.save()
        return Response(
            {
                "status": 200,
                "message": "data load success",
                "added": added,
            }
        )
    except:
        print("error while reading floodData")
        return Response(
            {
                "status": 404,
                "message": "error while reading floodData",
            }
        )
