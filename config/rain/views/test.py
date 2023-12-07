from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render


class Test(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "success!",
            }
        )


def testPage(request):
    return render(request, "index.html")
