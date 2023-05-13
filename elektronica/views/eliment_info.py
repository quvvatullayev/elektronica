from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Eliment_info,
    Eliments,
)
from ..serialization import (
    Eliment_infoSerializer,
    ElimentsSerializer,
)

class Eliment_infoList(APIView):
    def get(self, request:Request):
        eliment_info = Eliment_info.objects.all()
        serializer = Eliment_infoSerializer(eliment_info, many=True)
        return Response(serializer.data)

class Eliment_infoGet(APIView):
    def get(self, request:Request, eliments_id:int):
        eliment_info = Eliment_info.objects.get(eliment=eliments_id)
        serializer = Eliment_infoSerializer(eliment_info)
        return Response(serializer.data)