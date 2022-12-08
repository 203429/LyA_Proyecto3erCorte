from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class OperacionesView(APIView):
    def get(self, request, format=None):
        return Response("test", status=status.HTTP_200_OK)