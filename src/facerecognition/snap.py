import cv2
import os
from datetime import datetime
path = '/home/pi/Desktop/sesame/SESAME/src/frontend/src/assets/snapshots'
now = datetime.now()

def takeScreen(vs):
    snapshot = vs.read()
    dt = now.strftime('%d_%m_%Y___%H_%M_%S')
    savestr = path +'/'+'snapshot_'+dt+'.jpg'
    print(savestr)
    cv2.imwrite(savestr, snapshot)