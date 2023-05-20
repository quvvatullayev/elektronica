from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import render
from ..models import (
    Eliment_info,
    Eliments,
)
from ..serialization import (
    Eliment_infoSerializer,
    ElimentsSerializer,
)

class ElimentSorted(APIView):
    def get(self, request:Request):
        queryset = request.query_params.get('queryset')
        eliments = Eliments.objects.filter(description__icontains=queryset)
        data = ElimentsSerializer(eliments, many=True).data
        return Response(data)