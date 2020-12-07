from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openpay
# Create your views here.

class ChargeView(APIView):
    
    def post(self, request, *args, **kwargs):
        result=openpay.charges.create(request.data)
        return Response(result)