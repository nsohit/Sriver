# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:04:10 2020

@author: sohit
"""
import requests
import json
servername = "http://inoprex.com/post-esp-data.php"
api_key_value = "12345678"
sensorName = "tampa-nama"
sensorLocation = "Universitas_Raharja"
#data = "api_key=" + apiKeyValue + "&sensor=" + sensorName+ "&location=" + sensorLocation + "&value1=" + str(321)+"&value2=" + str(321)+"&value3=" + str(321)+ ""
data= "&sensor=" + sensorName+ "&location=" + sensorLocation + "&value1=" + str(123)+ "&value2=" + str(111) + "&value3=" + str(111) + ""
url = "http://inoprex.com/post-esp-data.php"
s='0.98'
val = 768
#data = { 'api_key' : apiKeyValue, 'ph' :s, 'load_balance' :val }
#print(type(data))

#dataJson = json.dumps(data)
#payload = {"json_payload": dataJson}
#url ='http://api.inoprex.com/server.php'
headers = {"Content-Type": "application/x-www-form-urlencoded"}
requests.post(url,data,headers)
response = requests.post(url,headers,data)
print(data)
print (response)
