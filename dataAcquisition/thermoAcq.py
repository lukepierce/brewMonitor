import http.client
import urllib.parse
import serial
import json
from time import localtime
import re

##TODO: Add timestamp to data points, model, serializer
##TODO: Remove MAX test print from Arduino Sketch

#Global State
decimal_re = re.compile(r"(?P<decimal>[0-9.]+)")
tty = 'ttyACM0'
datapoint = {}
datapoint['brew_name'] = "My Brown Nuts"
headers = {"Content-Type" : 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

if __name__ == '__main__':
    serial_conn = serial.Serial('/dev/' + tty, 9600)
    serial_conn.readline() #Gets the first line which is a test print
    http_conn = http.client.HTTPConnection('localhost', 8000)
    while True:
        line = serial_conn.readline()
        line = str(line)
        match = decimal_re.search(line)
        datapoint['temperature'] = match.group('decimal')
        datapointjson = json.dumps(datapoint)
        http_conn.request("PUT", "/thermo/", datapointjson, headers)
        response = http_conn.getresponse()
        str_response = response.readall().decode('utf-8')
        print(str_response)
        print(response.status, response.reason)
    serial_conn.close()
    http_conn.close()
