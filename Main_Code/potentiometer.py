from ADCDevice import *

class Potentiometer:
	def __init__(self, channel):
		self.channel = channel
		self.adc = ADS7830()
	def value(self):
		return self.adc.analogRead(self.channel)
