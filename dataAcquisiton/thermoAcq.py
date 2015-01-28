import http.client
import urllib.parse
import serial
import json
from time import localtime
from ast import literal_eval

##TODO: Add timestamp to data points, model, serializer

#Global State
tty = 'ttyACM0'
datapoint = {}
datapoint['brew_name'] = "My Brown Nuts"
headers = {"Content-Type" : 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

if __name__ == '__main__':
    serial_conn = serial.Serial('/dev/' + tty, 9600)
    serial_conn.readline() #Gets the first line which is a test print
    http_conn = http.client.HTTPConnection('localhost', 8000)
    while True:
        #literal eval strips the escape characters from readline
        datapoint['temperature'] = literal_eval(serial_conn.readline())
        datapointjson = json.dumps(datapoint)
        conn.request("PUT", "/thermo/", datapointjson, headers)
        response = conn.getresponse()
        str_response = response.readall().decode('utf-8')
        print(str_response)
        print(response.status, response.reason)
    serial_conn.close()
    http_conn.close()
