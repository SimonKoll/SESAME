import threading

from flask import Response
from flask import Flask
from flask import render_template
import time
import cv2
from imutils.video import VideoStream
import os

outputFrame = None
lock = threading.Lock()

app = Flask(__name__)
vs = VideoStream(src=0).start()  # 0 für Webcam, oder 1, oder 2
time.sleep(2.0)


def detect_face(args):
    # grab global references to the video stream, output frame, and
    # lock variables
    global vs, outputFrame, lock

    while True:
        # read the next frame from the video stream, resize it,
        # convert the frame to grayscale, and blur it
        success, frame = vs.read()

        """
        Face detection processing
        """
        os.system('python3 face_rec.py')
        """
        """
        
        with lock:
            outputFrame = frame.copy()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


def generate():
    # grab global references to the output frame and lock variables
    global outputFrame, lock
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if outputFrame is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
            # ensure the frame was successfully encoded
            if not flag:
                continue
        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


if __name__ == '__main__':
    # construct the argument parser and parse command line arguments
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--ip", type=str, required=True,
    #                help="ip address of the device")
    #ap.add_argument("-o", "--port", type=int, required=True,
    #                help="ephemeral port number of the server (1024 to 65535)")
    #ap.add_argument("-f", "--frame-count", type=int, default=32,
    #               help="# of frames used to construct the background model")
    #args = vars(ap.parse_args())
    # start a thread that will perform motion detection
    t = threading.Thread(target=detect_face, args=(32,))
    t.daemon = True
    t.start()
    # start the flask app
    app.run(debug=True,
            threaded=True, use_reloader=False)
# release the video stream pointer
vs.stop()