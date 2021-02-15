import RPi.GPIO as GPIO
import time
from generate_dataset import gendata
 
GPIO.setmode(GPIO.BCM)
 
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distanz():
    GPIO.output(GPIO_TRIGGER, True)
 
    time.sleep(0.00001)
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
            abstand = 49 
            print ("Gemessene Entfernung = %.1f cm" % abstand)
            if abstand < 50:
                print("Intruder alert")
                gendata()
            time.sleep(0.1)
 
    except KeyboardInterrupt:
        GPIO.cleanup()