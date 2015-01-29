'''
Created on Jan 27, 2015

@author: lukepierc
'''
'''
Created on Jan 15, 2015

@author: lukepierc
'''
import http.client
import urllib.parse
import json

if __name__ == '__main__':
    values = {'temperature' : '74',
              'brew_name': 'btubs'}
    data = json.dumps(values)
    conn = http.client.HTTPConnection('localhost', 8000)
    headers = {"Content-Type" : 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
    conn.request("PUT", "/thermo/", data, headers)
    response = conn.getresponse()
    str_response = response.readall().decode('utf-8')
    print(str_response)
    f = open('results.html', 'w')
    f.write(str_response)
    f.close()
    print(response.status, response.reason)
