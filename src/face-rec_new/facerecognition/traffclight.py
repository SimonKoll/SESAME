import time

import RPi.GPIO as GPIO


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)  # green
    GPIO.setup(23, GPIO.OUT)  # red
    GPIO.setup(24, GPIO.OUT)  # yellow


def loop():
    GPIO.output(23, True)
    time.sleep(1)
    GPIO.output(24, True)
    time.sleep(1)
    GPIO.output(23, False)
    GPIO.output(24, False)
    GPIO.output(25, True)
    time.sleep(1)
    GPIO.output(25, False)


setup()
try:
    while True:
        loop()
finally:
    GPIO.cleanup()
