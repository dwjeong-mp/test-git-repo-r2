import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

client = mqtt.Client()
client.connect("192.168.111.95", 1883, 60)

def on_connect(client, userdata, flag, rc): 
	print("IN!!!!!!!!!!!!!")
	client.subscribe("mkh")

def on_message(client, userdata, msg): 
	if 1 in msg.payload: 
		print("on")
		GPIO.output(40, 1)
	else :
		print("off!")
		GPIO.output(40, 0)


client.on_connect = on_connect
client.on_message = on_message

client.loop_forever() 
