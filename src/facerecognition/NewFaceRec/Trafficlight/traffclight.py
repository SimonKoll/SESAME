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


def loop():
    GPIO.output(redGPIO, True)
    time.sleep(1)
    GPIO.output(yellowGPIO, True)
    time.sleep(1)
    GPIO.output(redGPIO, False)
    GPIO.output(yellowGPIO, False)
    GPIO.output(greenGPIO, True)
    time.sleep(1)
    GPIO.output(greenGPIO, False)


setup()
try:
    while True:
        loop()
finally:
    GPIO.cleanup()
