import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
try:
  while True:
    p.ChangeDutyCycle(0.5)
    time.sleep(10)
    p.ChangeDutyCycle(12.5)
    time.sleep(10)
    p.ChangeDutyCycle(0.5)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()