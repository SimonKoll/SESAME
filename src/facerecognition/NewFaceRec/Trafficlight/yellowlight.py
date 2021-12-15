import time
import os
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


def yellow():
    GPIO.output(yellowGPIO, True)
    GPIO.output(redGPIO, False)
    GPIO.output(greenGPIO, False)


try:
    print("yellowlight")
finally:
    setup()
    yellow()