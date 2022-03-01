import time

import RPi.GPIO as GPIO

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 als PWM mit 50Hz


def spinClockwise():
    p.start(2.5)  # Initialisierung
    try:
        while True:
            p.ChangeDutyCycle(0.5)
            time.sleep(10)
            p.ChangeDutyCycle(12.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
    finally:
        GPIO.cleanup()


def spinCounterClockwise():
    p.start(2.5)  # Initialisierung
    try:
        while True:
            p.ChangeDutyCycle(0.5)
            time.sleep(10)
            p.ChangeDutyCycle(12.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
