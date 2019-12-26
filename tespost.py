
import requests
import json
servername = 'http://inoprex.com/post-esp-data.php'
apiKeyValue = 'tPmAT5Ab3j7F9'
sensorName = 'tampa-nama'
sensorLocation = 'Universitas_Raharja'
#data = 'api_key=' + apiKeyValue + '&sensor=' + sensorName+ '&location=' + sensorLocation + '&value1=' + str(321$
#url = 'http://inoprex.com/post-esp-data.php'
s="0.98"
val = 768
data = { 'api_key' : apiKeyValue, 'ph' :s, 'load_balance' :val }
print(type(data))

dataJson = json.dumps(data)
payload = {"json_payload": dataJson}
url ='http://api.inoprex.com/server.php'
headers = {'charset' : 'utf-8','Content-Type' : 'application/json'}
requests.post(url,dataJson,headers)
response = requests.post(url,headers,dataJson)
print(dataJson)
print (response)
