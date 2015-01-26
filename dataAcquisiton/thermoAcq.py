import serial
import json
from time import localtime, strftime

brewname = "My Brown Nuts"
f = open('workfile', 'w')
ser = serial.Serial('/dev/ttyACM0', 9600)
datapoints = 0



while True:
    datum = ser.readline()
    f.write(strftime("%Y-%m-%d %H:%M:%S", localtime()) + ', ' + datum)
    print(datum)
    datapoints += 1

f.close()
ser.close()
