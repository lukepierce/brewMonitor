import http.client
import urllib.parse
import serial
import json
import datetime
import re

##TODO: Remove MAX test print from Arduino Sketch

#Global State
decimal_re = re.compile(r"(?P<decimal>[0-9.]+)")
http_conn_addr = '192.168.1.102'
http_conn_port = '80'
tty = 'ttyACM0'
datapoint = {}
datapoint['brew_name'] = "My Brown Nuts"
headers = {"Content-Type" : 'application/x-www-form-urlencoded', 'Accept': 'application/json'}

if __name__ == '__main__':
    serial_conn = serial.Serial('/dev/' + tty, 9600)
    serial_conn.readline() #Gets the first line which is a test print
    http_conn = http.client.HTTPConnection(http_conn_addr + ':' + http_conn_port)
    while True:
        line = serial_conn.readline()
        line = str(line)
        match = decimal_re.search(line)
        datapoint['temperature'] = match.group('decimal')
        datapoint['time'] = datetime.datetime.now().isoformat()
        datapointjson = json.dumps(datapoint)
        try:
            http_conn.request("PUT", "/thermo/", datapointjson, headers)
            response = http_conn.getresponse()
        except http.client.BadStatusLine:
            print("Bad Status Line Exception Handled")
        else:
            str_response = response.readall().decode('utf-8')
            print(str_response)
            print(response.status, response.reason)
    serial_conn.close()
    http_conn.close()
