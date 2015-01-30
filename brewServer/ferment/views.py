from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Imports for using thermoAcq
import json
from time import localtime
from ferment.models import Data
# Rest Framework Imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO

def home(request):
    html = "<html><body><a href=data>data</a></body></html>"
    return HttpResponse(html)

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
