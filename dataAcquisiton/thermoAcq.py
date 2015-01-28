import http.client
import urllib.parse
import serial
import json
from time import localtime

datapoint['brew_name'] = "My Brown Nuts"

def serialbox(tty):
    '''
    Takes a 'tty' connection as input
    Returns a serial connection object
    Opens a serial connection to the arduino
    '''
    ser = serial.Serial('/dev/' + tty, 9600)
    return ser

if __name__ == '__main__'
    conn = serialbox('ttyACM0')
    while True:
        datapoint['temperature'] = ser.readline()
        datapoint['timestamp'] = localtime()
        datapointjson = json.dumps(datapoint)

    f.close()
    conn.close()
