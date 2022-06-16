import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


client = mqtt.Client()

client.connect("192.168.111.92", 1883, 60)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setwarnings(False)

def on_connect(client, userdata, flag, rc):
	print("Connected with rc:" + str(rc))
	client.subscribe("SH")

def on_message(client, userdata, msg):
	if 7 in msg.payload:
		print("ON!!!")
		GPIO.output(15, True)
	else :
		print("OFF!!")
		GPIO.output(15, False)

client.on_connect = on_connect
client.on_message = on_message


client.loop_forever()
