import RPi.GPIO as GPIO
import requests
import serial
import json
import time

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board$
GPIO.setwarnings(False) 
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # on

servername = 'http://inoprex.com/post-esp-data.php'
apiKeyValue = 'tPmAT5Ab3j7F9'
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
EMULATE_HX711=False
referenceUnit = -441

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
   print("Cleaning...")

   if not EMULATE_HX711:
        GPIO.cleanup()

   print("Bye!")
   sys.exit()
hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()
while True:
   val =max (0,int(hx.get_weight(5))) #timbangan
   s=ser.readline().decode().strip('\r\n') #ph
   data = { 'api_key' : apiKeyValue, 'ph' :s, 'load_ba$
   dataJson = json.dumps(data)
   payload = {"json_payload": dataJson}
   url ='http://api.inoprex.com/server.php'
   headers = {'charset' : 'utf-8','Content-Type' : 'ap$
   requests.post(url,dataJson,headers)
   response = requests.post(url,headers,dataJson)
   print(dataJson)
   print (response)
   if val > 4000:
      GPIO.cleanup()

