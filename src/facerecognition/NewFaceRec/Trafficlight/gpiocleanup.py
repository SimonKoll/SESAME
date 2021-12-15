import time

import RPi.GPIO as GPIO
redGPIO = 16
yellowGPIO = 20
greenGPIO = 21


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(greenGPIO, GPIO.OUT)  # green
    GPIO.setup(redGPIO, GPIO.OUT)  # red
    GPIO.setup(yellowGPIO, GPIO.OUT)  # yellow


try:
    setup()
finally:
    GPIO.cleanup()
