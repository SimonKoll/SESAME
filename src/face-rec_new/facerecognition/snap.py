from datetime import datetime

import cv2

path = '/home/pi/Desktop/'
now = datetime.now()


def takeScreen(vs):
    snapshot = vs.read()
    dt = now.strftime('%d_%m_%Y___%H_%M_%S')
    savestr = path + '/' + 'snapshot_' + dt + '.jpg'
    print(savestr)
    cv2.imwrite(savestr, snapshot)
