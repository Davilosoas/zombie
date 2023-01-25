from rest_framework import serializers
from .models import Survivor
from rest_framework.response import Response
from rest_framework import status

class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor
        fields = '__all__'
