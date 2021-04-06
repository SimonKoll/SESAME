import pygetwindow
import pyautogui
from PIL import Image
from datetime import datetime

def takeSnap():
    now = datetime.now()
    dt = now.strftime("%d-%m-%Y-%H-%M-%S")
    savestr='/home/pi/Desktop/Sesame/src/facerecognition/snapshots/snapshot_'+dt+'.jpeg'
    print(savestr)
    titles = pygetwindow.getAllTitles()
    x1,y1,width,height = pygetwindow.getWindowGeometry("faceRec")
    x2=x1+width
    y2=y1+height

    pyautogui.screenshot(savestr)
    im = Image.open(savestr)
    im=im.crop((x1,y1,x2,y2))
    im.save(savestr)
