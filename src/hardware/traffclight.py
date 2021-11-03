import RPi.GPIO as GPIO
import time
import signal
import sys

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
	GPIO.output(22, False)
	GPIO.output(18, False)
	GPIO.output(16, False)
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, allLightsOff)

# Loop forever
while True:
	# Red
	GPIO.output(9, True)
	time.sleep(3)

	# Red and amber
	GPIO.output(18, True)
	time.sleep(1)
	
	# Green
	GPIO.output(9, False)
	GPIO.output(18, False)
	GPIO.output(16, True)
	time.sleep(5)
	
	# Amber
	GPIO.output(16, False)
	GPIO.output(18, True)
	time.sleep(2)
	
	# Amber off (red comes on at top of loop)
	GPIO.output(18, False)

