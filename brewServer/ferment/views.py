from django.shortcuts import render
from django.http import HttpResponse
#Imports for using thermoAcq
import json
from time import localtime
from ferment.models import Data
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
from django.shortcuts import render_to_response



def home(request):
    return HttpResponse('hello world')

def viewData(request):
    return render_to_response('data.html',  {'data': Data.objects.all()})

class Thermo(APIView):
    def put(self, request,format=None):
        stream = BytesIO(request.read())
        print(str(stream))
        data = JSONParser().parse(stream)
        print(data)
        Data.objects.create(temperature=data['temperature'], brew_name=data['brew_name'], time=data['time'])
        return Response("It fucking works")
