from django.shortcuts import render
from django.http import HttpResponse
#Imports for using thermoAcq
import json
from time import localtime
from ferment.models import Data
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView




def home(request):
    return HttpResponse('hello world')

def thermo(APIView):
    def put(self, format=None):
        stream = BytesIO(request.read())
        data = JSONParser().parse(stream)
        Data.objects.create(temperature=data['temperature'], brew_name=data['brew_name'])
        return Response("It fucking works")
