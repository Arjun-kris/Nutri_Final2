from flask import Flask, render_template, Response, request, flash, redirect
import cv2
import datetime
import os
import glob
from PIL import Image
from keras.models import load_model
import pandas as pd
from keras.utils import img_to_array
import numpy as np

global capture, rec_frame, out, analyse
capture = 0
analyse = 0


# make shots directory to save pics
try:
    os.mkdir('./shots')
except OSError as error:
    pass

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"
app.config['SESSION_TYPE'] = 'filesystem'

camera = cv2.VideoCapture(0)
_, img = camera.read()
(fh, fw) = img.shape[:2]
captured_frame = Image.new('RGB', (fw, fh))
analysed_frame = Image.new('RGB', (fw, fh))
food_label = ''
km = load_model(r'food_detect_model.hdf5', compile=False)
df = pd.read_csv('calorie_data.csv')
e = list(df['categories'].values)

def gen_frames():  # generate frame by frame from camera
    global out, capture, rec_frame, captured_frame, analysed_frame, analyse
    while True:
        success, frame = camera.read()
        if success:
            if capture:
                capture = 0
                now = datetime.datetime.now()
                p = os.path.sep.join(['shots', "shot_{}.png".format(str(now).replace(":", ''))])
                cv2.imwrite(p, frame)
                captured_frame = frame

            if analyse:
                analyse = 0
                ts = 0
                found = None
                for file_name in glob.glob('D:/final project 2/Latest_Nutri2New/Latest_Nutri2/shots/*'):
                    fts = os.path.getmtime(file_name)
                    if fts > ts:
                        ts = fts
                        found = file_name
                frame = cv2.imread(found)
                analysed_frame = frame

            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame, 1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass

        else:
            pass


def cap_snap():  # generate frame by frame from camera
    global captured_frame
    ret, buffer = cv2.imencode('.jpg', cv2.flip(captured_frame, 1))
    frame = buffer.tobytes()
    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return redirect('/')


def classify(frame):
    global food_label
    roi = cv2.resize(frame, (299, 299))
    roi = img_to_array(roi)
    roi = np.expand_dims(roi, axis=0)
    roi /= 255.
    pred = km.predict(roi)
    ind = pred.argmax()
    food_label = e[ind]
    print(e[ind])


def analy_snap():  # generate frame by frame from camera
    global analysed_frame, km, df, e
    classify(analysed_frame)
    ret, buffer = cv2.imencode('.jpg', cv2.flip(analysed_frame, 1))
    frame = buffer.tobytes()
    yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return redirect('/')


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/capture_snap')
def capture_snap():
    return Response(cap_snap(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/analyse_snap')
def analyse_snap():
    global food_label
    flash(food_label)
    return Response(analy_snap(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/requests', methods=['POST', 'GET'])
def tasks():
    global camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture = 1
        if request.form.get('click') == 'Analyse':
            global analyse
            analyse = 1
    elif request.method == 'GET':
        return render_template('index1.html')
    return render_template('index1.html')


if __name__ == '__main__':
    app.run(port=5400)

