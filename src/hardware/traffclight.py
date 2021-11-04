import RPi.GPIO as GPIO
import time
def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25,GPIO.OUT)
def loop():
        GPIO.output(25,True)
        time.sleep(1)
        GPIO.output(25,False)
        time.sleep(1)
setup()
try:
    while True:
        loop()
finally:
    GPIO.cleanup()