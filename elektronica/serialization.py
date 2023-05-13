from rest_framework import serializers
from .models import (
    Eliments,
    Eliment_info,
)

class ElimentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eliments
        fields = "__all__"

class Eliment_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eliment_info
        fields = "__all__"