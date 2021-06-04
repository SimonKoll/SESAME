import os

def countUsers():
    APP_FOLDER = '/home/pi/Desktop/sesame/SESAME/src/facerecognition/dataset'
    totalDir = 0
    for base, dirs, files in os.walk(APP_FOLDER):
        for directories in dirs:
            totalDir += 1
    print('Total Number of directories',totalDir)
    return totalDir
