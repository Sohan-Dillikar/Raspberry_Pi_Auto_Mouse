import pyautogui
import RPi.GPIO as GPIO
from time import sleep
from joystick import Joystick
from potentiometer import Potentiometer
from distance_sensor import DistanceSensor

pyautogui.FAILSAFE = False

def to_percent(values):
	return [(value * 100) / 254 for value in values]

def setup():
	global joystick, mouse_control, scroll_control, distance_sensor
	GPIO.setmode(GPIO.BOARD)
	joystick = Joystick(7, 0, 1)
	mouse_control = Potentiometer(2)
	scroll_control = Potentiometer(3)
	distance_sensor = DistanceSensor(35, 37)
	
def loop():
	mouse_x, mouse_y = pyautogui.position()
	while True:
		joystick_x, joystick_y = to_percent(joystick.pos())
		mouse_speed = to_percent([mouse_control.value()])[0]
		scroll_speed = to_percent([scroll_control.value()])[0] / 5
		distance = distance_sensor.distance()
		if joystick.clicked():
			pyautogui.click()
			sleep(1)
		if joystick_x <= 37:
			mouse_x -= mouse_speed
		elif joystick_x >= 63:
			mouse_x += mouse_speed
		if joystick_y <= 37:
			mouse_y -= mouse_speed
		elif joystick_y >= 63:
			mouse_y += mouse_speed
		if distance <= 5:
			pyautogui.scroll(-scroll_speed)
		elif distance > 5 and distance <= 10:
			pyautogui.scroll(scroll_speed)
		pyautogui.moveTo(mouse_x, mouse_y)
		
def destroy():
	GPIO.cleanup()
	
if __name__ == '__main__':
	print('Program has started...')
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		print('Bye!')
	finally:
		destroy()
