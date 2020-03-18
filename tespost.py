import requests
import json
servername = 'http://inoprex.com/post-esp-data.php'
apiKeyValue = 'tPmAT5Ab3j7F9'
sensorName = 'tampa-nama'
sensorLocation = 'Universitas_Raharja'
#data = 'api_key=' + apiKeyValue + '&sensor=' + sensorName+ '&location=' + sensorLocation + '&value1=' + str(321)+ '&value2=' + str(987) + '&value3=' + str(123) + ""
url = 'http://inoprex.com/post-esp-data.php'
'''
ldrvalue = '50'
data='ldrvalue='+ldrvalue
'''
#data = { 'api_key' : apiKeyValue, 'sensor' : "12", 'location' : "12",'value1':"12", 'value2':"12",'value3':"12" }
#dataJson = json.dumps(data)
#payload = {"json_payload": dataJson}
#url ='http://www.inoprex.com/server.php'
#data = "{\"value1\":\"19\",\"value2\":\"67\",\"value3\":\"78\"}"
data="{\"api_key\"=\"tPmAT5Ab3j7F9\",\"sensor\"=\"abs\",\"location\"=\"acv\",\"value1\"=\"19\",\"value2\"=\"67\",\"value3\"=\"78\",\"\"}"
headers = {'Content-Type':'application/json'}
requests.post(url,headers=headers,data=data)
response=requests.post(url,headers=headers,data=data)
print(response)
print(data)
 #"{\"api_key\":\"tPmAT5Ab3j7F9\","\"value1\":\"19\",\"value2\":\"67\",\"value3\":\"78\"}"

