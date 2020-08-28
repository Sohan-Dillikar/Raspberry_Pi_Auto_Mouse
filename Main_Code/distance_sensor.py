import RPi.GPIO as GPIO
from time import time, sleep

class DistanceSensor:
	def __init__(self, trigPin, echoPin):
		GPIO.setup(trigPin, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(echoPin, GPIO.IN)
		self.trigPin = trigPin
		self.echoPin = echoPin
	def distance(self):
		GPIO.output(self.trigPin, GPIO.HIGH)
		sleep(0.00001)
		GPIO.output(self.trigPin, GPIO.LOW)
		while not GPIO.input(self.echoPin):
			start = time()
		while GPIO.input(self.echoPin):
			end = time()
		try:
			return (end - start) / 0.000058
		except UnboundLocalError:
			return 11
