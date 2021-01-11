from flask import Response, Flask
import cv2 as cv
import logging

log_file = "video.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d %(threadName)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

vs = cv.VideoCapture(0)

def generate_stream():
    while True:
        rc, frame = vs.read()
        (rc, outFrame) = cv.imencode(".jpg", frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(outFrame) + b'\r\n')

@app.route("/stream")
def video_feed():
    return Response(generate_stream(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=False, use_reloader=False)