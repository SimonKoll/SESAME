import os
import time

import RPi.GPIO as GPIO
from colorzero import Color
from gpiozero import RGBLED

led = RGBLED(red=17, green=27, blue=22)
GPIO.setmode(GPIO.BCM)

led.color = Color(128, 128, 128)

GPIO_TRIGGER = 21
GPIO_ECHO = 20

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distanz():
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.0005)
    GPIO.output(GPIO_TRIGGER, False)

    StartZeit = time.time()
    StopZeit = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()

    TimeElapsed = StopZeit - StartZeit

    distanz = (TimeElapsed * 34300) / 2

    return distanz


if __name__ == '__main__':
    try:
        while True:
            abstand = distanz()
            print("Gemessene Entfernung = %.1f cm" % abstand)
            if abstand < 100:
                led.color = Color(128, 128, 128)
                time.sleep(2)

                if abstand < 50:
                    print("Intruder alert")
                    led.color = Color(128, 0, 0)
                    os.system('python3 face_rec.py')
                    # gendata()
                else:
                    led.color = Color(128, 128, 128)
                time.sleep(0.5)

    except KeyboardInterrupt:
        GPIO.cleanup()
