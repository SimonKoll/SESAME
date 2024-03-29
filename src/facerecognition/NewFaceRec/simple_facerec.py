import face_recognition
import cv2
import os
import glob
import numpy as np
from datetime import datetime
import time
from pymongo import MongoClient
class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        # Resize frame for a faster speed
        self.frame_resizing = 0.25
        self.countUnknown = 0
        self.countKnown = 0
        self.path = '/home/pi/Desktop/NewFaceRec/Snapshots'
        self.client = MongoClient("mongodb+srv://sesame:sesame2021@cluster0.5zncd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["sesame"]
        self.collection = self.db["entrants"]



    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encoding images loaded")

    def detect_known_faces(self, frame, cap):
        os.system('python Trafficlight/yellowlight.py')
        small_frame = cv2.resize(
            frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                self.known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(
                self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                self.countKnown = self.countKnown+1
                print("wrong count")
                print(self.countKnown)
                if(self.countKnown > 5):
                    now = datetime.now()
                    dt_string = now.strftime("%d.%m.%Y / %H:%M")
                    entrant = {"name": name, "time": dt_string}
                    x = self.collection.insert_one(entrant)
                    print(x.inserted_id)
                    os.system('python Trafficlight/greenlight.py')
                    os.system('python Motor/motorClockwise.py')
                    time.sleep(10)
                    os.system('python Motor/motorCounterClockwise.py')
                    # activate motor
                
            face_names.append(name)
            if(name == "Unknown"):
                print("unknown")
                self.countUnknown = self.countUnknown+1
                print("wrong count")
                print(self.countUnknown)
                if(self.countUnknown > 10):
                    #now = datetime.now()
                    #snapshot = cap.read()
                    #dt = now.strftime('%d_%m_%Y___%H_%M_%S')
                    #savestr = self.path + '/' + 'snapshot_' + dt + '.jpg'
                    #print(savestr)
                    #cv2.imwrite(savestr, snapshot)
                    os.system('python Trafficlight/redlight.py')
                    
                    # save unknown entrant
                    # do not open door

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
