from django.shortcuts import render
from django.http import HttpResponse
#Imports for using thermoAcq
import serial
import json
from time import localtime
# Create your views here.

def home(request):
    return HttpResponse('hello world')

def thermo(request):
    brewname = "My Brown Nuts"
    ser = serial.Serial('/dev/ttyACM0', 9600)
    datapoint = {'temperature': None,
                 'timestamp': None,
                 'brewname': brewname}
    f.close()
    ser.close()
    return HttpResponse(datapoint['brewname'])
