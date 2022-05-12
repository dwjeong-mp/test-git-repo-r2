import RPi.GPIO as GPIO
import time
led_pin = 4 #GPIO 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
for i in range(100):
	GPIO.output(led_pin,1)
	time.sleep(0.03)
	GPIO.output(led_pin,0)
	time.sleep(0.03)
GPIO.cleanup()
