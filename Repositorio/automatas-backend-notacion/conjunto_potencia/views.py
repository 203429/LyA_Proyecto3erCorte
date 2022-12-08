from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Example(APIView):
    def get(self, request, format=None):
        return Response("Hola mundo desde conjunto potencia", status=status.HTTP_200_OK)