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

class Eliment_infoList(APIView):
    def get(self, request:Request):
        eliment_info = Eliment_info.objects.all()
        serializer = Eliment_infoSerializer(eliment_info, many=True)
        return Response(serializer.data)

class Eliment_infoGet(APIView):
    def get(self, request:Request, eliments_id:int):
        eliment_info = Eliment_info.objects.get(eliment=eliments_id)
        serializer = Eliment_infoSerializer(eliment_info)
        data = serializer.data
        data['values'] = data['values'].split()
        print(data)
        return render(request, 'eliment_info.html', {'eliment_info': data})
    
class ElimentsCount(APIView):
    def post(self, request:Request, pk:int):
        data = request.data

        eliment = Eliment_info.objects.get(pk=pk)
        eliment_data = Eliment_infoSerializer(eliment).data

        eliment_info = Eliment_info.objects.get(id=pk)
        serializer = Eliment_infoSerializer(eliment_info)

        response = serializer.data
        response['values'] = response['values'].split()
        formula = eliment_data['formula_text']
        try:
            variables = data.copy()
            del eliment_data['formula']
            
            for variable, value in variables.items():
                formula = formula.replace(variable, str(value))
            
            result = eval(formula)
        except NameError:
            result = 'NameError'
        print(response)
        return render(request, 'eliment_count.html', {'eliment_info': response, 'result': result})