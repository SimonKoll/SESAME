from gpiozero import Button, RGBLED
from colorzero import Color
import time, requests
import os

update_period = 10
led = RGBLED(red=18, green=23, blue=24)
button = Button(25)

buttonCount = 0
lastButtonState = 1
lastButtonPress = 0
led.color = Color(128,128,128)

def pressed():
    global buttonCount
    buttonCount=buttonCount+1
    
    if buttonCount == 4: # Rest the buttonCount to 0 once it has reached 3
        buttonCount = 0

    if buttonCount == 0: # off state
        led.color = Color(0,0,0)
        print("I am Off")

    if buttonCount == 1: # Red state
        led.color = Color(128,0,0)
        print("I am Red")
        os.system('python3 face_rec.py')
        

    if buttonCount == 2: #Green state
        led.color = Color(0,128,0)
        print("I am Green")

    if buttonCount == 3: # Blue state
        led.color = Color(0,0,128)
        print("I am Blue")
    
button.when_pressed = pressed

while True:
    try:
        print("")
    except Exception as e:
        print(e)
    time.sleep(update_period)
