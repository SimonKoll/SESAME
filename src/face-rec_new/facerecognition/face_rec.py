from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
from colorzero import Color
from datetime import datetime
from datetime import date
import snap as snap
from stopStream import pressQToStop
#import snapshot as takeSnaps
#import snapshot1 as snaps
import os
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

from pymongo import MongoClient


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)  # green
GPIO.setup(23, GPIO.OUT)  # red
GPIO.setup(24, GPIO.OUT)  # yellow

global thres
thres = 0

path = '/home/pi/Desktop/NewFaceRec/Snapshots'
client = MongoClient(
    "mongodb+srv://sesame:sesame2021@cluster0.5zncd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["entrants"]
collection = db["entrants"]
currentname = "unknown"
encodingsP = "encodings.pickle"
cascade = "haarcascade_frontalface_default.xml"

print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())
detector = cv2.CascadeClassifier(cascade)

print("[INFO] starting video stream...")
vs = VideoStream(src=1).start()
time.sleep(2.0)
running = True

fps = FPS().start()
while running:
    GPIO.output(23, False)
    GPIO.output(24, True)
    GPIO.output(25, False)
    frame = vs.read()
    frame = imutils.resize(frame, width=600)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    rects = detector.detectMultiScale(gray, scaleFactor=1.1,
                                      minNeighbors=5, minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE)

    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        name = "Unknown"
        GPIO.output(23, True)
        GPIO.output(24, False)
        GPIO.output(25, False)
        thres += 1
        print(thres)

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)

            if currentname != name:
                currentname = name
                print(currentname)
                names.append(name)
                GPIO.output(23, False)
                GPIO.output(24, False)
                GPIO.output(25, True)
                now = datetime.now()
                dt_string = now.strftime("%d.%m.%Y / %H:%M")
                entrant = {"name": name, "time": dt_string}
                x = collection.insert_one(entrant)
                print(x.inserted_id)
                os.system('python Motor/motorClockwise.py')
                time.sleep(10)
                os.system('python Motor/motorCounterClockwise.py')
                # activate motor
                running = False
        names.append(name)
        if thres > 10:
            print("TAKE SCREENSHOT --- Thres")
            snap.takeScreen(vs)
            now = datetime.now()
            dt_string = now.strftime("%d.%m.%Y / %H:%M")
            entrant = {"name": "UNKNOWN", "time": dt_string}
            x = collection.insert_one(entrant)
            print(x.inserted_id)
            pressQToStop()
            print(thres)
            thres = 0
            running = False

    for ((top, right, bottom, left), name) in zip(boxes, names):
        cv2.rectangle(frame, (left, top), (right, bottom),
                      (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                    .8, (255, 0, 0), 2)

    cv2.imshow("faceRec", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()
vs.stream.stream.release()

os.system("python3 distance.py")
