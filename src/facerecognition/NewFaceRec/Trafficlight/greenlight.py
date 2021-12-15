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


def green():
    GPIO.output(yellowGPIO, False)
    GPIO.output(redGPIO, False)
    GPIO.output(greenGPIO, True)


try:
    print("greenlight")
finally:
    setup()
    green()
    time.sleep(3)
    os.system("python stopStream.py")