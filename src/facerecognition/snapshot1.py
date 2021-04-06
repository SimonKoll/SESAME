import os.path
import pyscreenshot
import pyautogui
from datetime import datetime
def takeSnap(windowName):
    now = datetime.now()
    dt = now.strftime("%d-%m-%Y-%H-%M-%S")
    save_path = '/home/pi/Desktop/Sesame/src/facerecognition/snapshots'
    width, height= pyautogui.size()
    # im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
    image = pyscreenshot.grab(bbox=(10, 10, 800, 800))
    print(width)
    print(height)
    savestr='/home/pi/Desktop/Sesame/src/facerecognition/snapshots/snapshot_'+dt+'.jpeg'
    print(savestr)
    # To save the screenshot
    image.save(savestr, 'JPEG')

