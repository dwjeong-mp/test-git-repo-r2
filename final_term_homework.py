import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

mqttc = mqtt.Client()
mqttc.connect("192.168.111.95", 1883, 60)

def connected(client, userdata, flag, rc): 
	print("Connected in successfully!!")
	client.subscribe("dw")

def message_revise(client, userdata, msg): 
	if 1 in msg.payload: 
		print("Correct signal published from phone!")
		GPIO.output(8, True)
	else :
		print("Incorrect sinal was published on phone!")
		GPIO.output(8, False)


mqttc.on_connect = connected
mqttc.on_message = message_revise

mqttc.loop_forever() 
