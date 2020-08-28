import RPi.GPIO as GPIO
from ADCDevice import *

class Joystick:
	def __init__(self, button_pin, channel_x, channel_y):
		GPIO.setup(button_pin, GPIO.IN, GPIO.PUD_UP)
		self.adc = ADS7830()
		self.button_pin = button_pin
		self.channel_x = channel_x
		self.channel_y = channel_y
	def pos(self):
		x_pos = self.adc.analogRead(self.channel_x)
		y_pos = self.adc.analogRead(self.channel_y)
		return x_pos, y_pos
	def clicked(self):
		if GPIO.input(self.button_pin) == GPIO.LOW:
			return True
		return False
