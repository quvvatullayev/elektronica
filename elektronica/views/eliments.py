from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.shortcuts import render
from ..models import (
    Eliments,
)
from ..serialization import (
    ElimentsSerializer,
)

class ElimentsList(APIView):
    def get(self, request:Request):
        eliments = Eliments.objects.all()
        serializer = ElimentsSerializer(eliments, many=True)
        return render(request, 'elements.html', {'elements': serializer.data})