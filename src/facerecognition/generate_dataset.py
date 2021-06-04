import cv2
import os
import os.path
import time
from train_model import training
from count_folders import countUsers
def gendata():
    print("enter username: ")
    totalUsers = countUsers()
    newUser = totalUsers+1
    name = "user"+str(newUser)
    face_dir = "/home/pi/Desktop/sesame/SESAME/src/facerecognition"
    parent_dir = "/home/pi/Desktop/sesame/SESAME/src/facerecognition/dataset"

    path = os.path.join(parent_dir, name)
    os.mkdir(path)
    print("Directory '% s' created" % name)
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Smile, you are on camera", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Smile, you are on camera", 1280, 720)

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Smile, you are on camera", frame)


        time.sleep(5)
        print("first picture in 5 seconds")

        for i in range(10):
            time.sleep(1)
            img_name = "dataset/" + name + "/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()


    cv2.destroyAllWindows()
    print('running python3 train_model.training '+name)
    training(name)
