from gpiozero import Servo
from time import sleep

from gpiozero.pins.gpio import PiGPIOFactory

factory = PiGPIOFactory()
servo = Servo(17, min_pulse_width=0.5/1000,
              max_pulse_width=2.5/1000, pin_factory=factory)


print("Start in the middle")
servo.mid()
sleep(5)
print("Got to min")
servo.min()
sleep(5)
print("Got to Max")
servo.max()
sleep(5)
print("Got to mid")
servo.mid()

sleep(5)

servo.value = None
