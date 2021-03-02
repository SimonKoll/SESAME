from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import imutils
import pickle
import time
import cv2
from gpiozero import Button, RGBLED, Buzzer
from colorzero import Color
import json
from datetime import datetime
from datetime import date
import writeJSON as wJSON		
#import RPi.GPIO as GPIO
#import time
import os
from time import sleep

buzzer = Buzzer(16)

#json.load('entries.json')
led = RGBLED(red=18, green=23, blue=24)
button = Button(25)

#buzzer_pin = 16
#
#GPIO.setup(16, GPIO.OUT)
#
#notes = {
#	'B0' : 31,
#	'C1' : 33, 'CS1' : 35,
#	'D1' : 37, 'DS1' : 39,
#	'EB1' : 39,
#	'E1' : 41,
#	'F1' : 44, 'FS1' : 46,
#	'G1' : 49, 'GS1' : 52,
#	'A1' : 55, 'AS1' : 58,
#	'BB1' : 58,
#	'B1' : 62,
#	'C2' : 65, 'CS2' : 69,
#	'D2' : 73, 'DS2' : 78,
#	'EB2' : 78,
#	'E2' : 82,
#	'F2' : 87, 'FS2' : 93,
#	'G2' : 98, 'GS2' : 104,
#	'A2' : 110, 'AS2' : 117,
#	'BB2' : 123,
#	'B2' : 123,
#	'C3' : 131, 'CS3' : 139,
#	'D3' : 147, 'DS3' : 156,
#	'EB3' : 156,
#	'E3' : 165,
#	'F3' : 175, 'FS3' : 185,
#	'G3' : 196, 'GS3' : 208,
#	'A3' : 220, 'AS3' : 233,
#	'BB3' : 233,
#	'B3' : 247,
#	'C4' : 262, 'CS4' : 277,
#	'D4' : 294, 'DS4' : 311,
#	'EB4' : 311,
#	'E4' : 330,
#	'F4' : 349, 'FS4' : 370,
#	'G4' : 392, 'GS4' : 415,
#	'A4' : 440, 'AS4' : 466,
#	'BB4' : 466,
#	'B4' : 494,
#	'C5' : 523, 'CS5' : 554,
#	'D5' : 587, 'DS5' : 622,
#	'EB5' : 622,
#	'E5' : 659,
#	'F5' : 698, 'FS5' : 740,
#	'G5' : 784, 'GS5' : 831,
#	'A5' : 880, 'AS5' : 932,
#	'BB5' : 932,
#	'B5' : 988,
#	'C6' : 1047, 'CS6' : 1109,
#	'D6' : 1175, 'DS6' : 1245,
#	'EB6' : 1245,
#	'E6' : 1319,
#	'F6' : 1397, 'FS6' : 1480,
#	'G6' : 1568, 'GS6' : 1661,
#	'A6' : 1760, 'AS6' : 1865,
#	'BB6' : 1865,
#	'B6' : 1976,
#	'C7' : 2093, 'CS7' : 2217,
#	'D7' : 2349, 'DS7' : 2489,
#	'EB7' : 2489,
#	'E7' : 2637,
#	'F7' : 2794, 'FS7' : 2960,
#	'G7' : 3136, 'GS7' : 3322,
#	'A7' : 3520, 'AS7' : 3729,
#	'BB7' : 3729,
#	'B7' : 3951,
#	'C8' : 4186, 'CS8' : 4435,
#	'D8' : 4699, 'DS8' : 4978
#}
#melody = [
#  notes['E7'], notes['E7'], 0, notes['E7'],
#  0, notes['C7'], notes['E7'], 0,
#  notes['G7'], 0, 0,  0,
#  notes['G6'], 0, 0, 0,
# 
#  notes['C7'], 0, 0, notes['G6'],
#  0, 0, notes['E6'], 0,
#  0, notes['A6'], 0, notes['B6'],
#  0, notes['AS6'], notes['A6'], 0,
# 
#  notes['G6'], notes['E7'], notes['G7'],
#  notes['A7'], 0, notes['F7'], notes['G7'],
#  0, notes['E7'], 0, notes['C7'],
#  notes['D7'], notes['B6'], 0, 0,
# 
#  notes['C7'], 0, 0, notes['G6'],
#  0, 0, notes['E6'], 0,
#  0, notes['A6'], 0, notes['B6'],
#  0, notes['AS6'], notes['A6'], 0,
# 
#  notes['G6'], notes['E7'], notes['G7'],
#  notes['A7'], 0, notes['F7'], notes['G7'],
#  0, notes['E7'], 0, notes['C7'],
#  notes['D7'], notes['B6'], 0, 0
#]
#tempo = [
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
# 
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
# 
#  9, 9, 9,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
# 
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#
#  9, 9, 9,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#  12, 12, 12, 12,
#]
#crazy_frog_melody = [
#	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
#	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
#	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
#	notes['A4'],0,
#	
#	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
#	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
#	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
#	notes['A4'],0,
#	
#	
#	notes['A3'], notes['G3'], notes['E3'], notes['D3'],
#	
#	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
#	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
#	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
#	notes['A4'],
#]
#crazy_frog_tempo = [
#	2,4,4,8,4,4,4,
#	2,4,4,8,4,4,4,
#	4,4,4,8,4,8,4,4,
#	1,4,
#	
#	2,4,4,8,4,4,4,
#	2,4,4,8,4,4,4,
#	4,4,4,8,4,8,4,4,
#	1,4,
#	
#	8,4,4,4,
#	
#	2,4,4,8,4,4,4,
#	2,4,4,8,4,4,4,
#	4,4,4,8,4,8,4,4,
#	1,
#]

#def buzz(frequency, length):	
#
#	if(frequency==0):
#		time.sleep(length)
#		return
#	period = 1.0 / frequency 		 
#	delayValue = period / 2		
#	numCycles = int(length * frequency)
#	
#	for i in range(numCycles):		
#		GPIO.output(buzzer_pin, True)	 
#		time.sleep(delayValue)		
#		GPIO.output(buzzer_pin, False)		
#		time.sleep(delayValue)		
#
#def setup():
#	GPIO.setmode(GPIO.BCM)
#	GPIO.setup(buzzer_pin, GPIO.IN)
#	GPIO.setup(buzzer_pin, GPIO.OUT)
#	
#def destroy():
#	GPIO.cleanup()		
#
#def play(melody,tempo,pause,pace=0.800):
#	
#	for i in range(0, len(melody)):		
#		
#		noteDuration = pace/tempo[i]
#		buzz(melody[i],noteDuration)
#		
#		pauseBetweenNotes = noteDuration * pause
#		time.sleep(pauseBetweenNotes)
#

currentname = "unknown"
encodingsP = "encodings.pickle"
cascade = "haarcascade_frontalface_default.xml"

print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())
detector = cv2.CascadeClassifier(cascade)

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

fps = FPS().start()
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=800)
	
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
		led.color = Color(128,0,0)
		
            
		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
				led.color = Color(0,128,0)

			name = max(counts, key=counts.get)
			
			if currentname != name:
				currentname = name
				print(currentname)
				names.append(name)
				for i in range(5):
					buzzer.on()
					sleep(1)
					buzzer.off()
					sleep(1)
				wJSON.writeEntriesToJson(currentname)
		#play(crazy_frog_melody, crazy_frog_tempo, 0.30, 0.900)
		#os.system('python3 buzzer.py')

       
	for ((top, right, bottom, left), name) in zip(boxes, names):
		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			.8, (255, 0, 0), 2)

	cv2.imshow("Facial Recognition is Running", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

	fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()
