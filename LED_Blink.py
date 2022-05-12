#-*- coding: utf-9 -*-

import RPi.GPIO as GPIO
import time
led_pin = 4 #GPIO 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.out)
for i in range(10):
	GPIO.output(led_pin,1)
	time.sleep(1)
	GPIO.output(led_pin,0)
	time.sleep(1)
GPIO.cleanup()
