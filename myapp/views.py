from django.shortcuts import render
from rest_framework import views
from .models import Survivor
from .serializers import SurvivorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def test_view(request):
    return Response({"message": "Django Rest Framework is working"})
    
class SurvivorView(views.APIView):
    def post(self, request, format=None):
        serializer = SurvivorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
