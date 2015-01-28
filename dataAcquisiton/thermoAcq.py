import http.client
import urllib.parse
import serial
import json
from time import localtime

##TODO: Add timestamp to data points, model, serializer

#Global State
tty = 'ttyACM0'
datapoint['brew_name'] = "My Brown Nuts"
headers = {"Content-Type" : 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

if __name__ == '__main__'
    serial_conn = serial.Serial('/dev/' + tty, 9600)
    http_conn = http.client.HTTPConnection('localhost', 8000)
    while True:
        datapoint['temperature'] = ser.readline()
        datapointjson = json.dumps(datapoint)
        conn.request("PUT", "/thermo/", datapoint, headers)
        response = conn.getresponse()
        str_response = response.readall().decode('utf-8')
        print(str_response)
        print(response.status, response.reason)
    f.close()
    conn.close()
