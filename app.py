from email.policy import default
from fileinput import filename
import mimetypes
from urllib import request
from io import BytesIO
from django.shortcuts import redirect
from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import cv2
import os
import io
from flask import *
from pathlib import Path
import time
import numpy as np
import sqlite3
from PIL import Image
from datetime import timedelta

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///image.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

vc = cv2.VideoCapture(0)

def gen_video(aadharno, name):
    userId=aadharno
    userName=name
    img = cv2.imread("./dataset/{}/{}".format(aadharno, "image.jpeg"))
    imgId=0
    count=0
    coords=[0,0,0,0]
    new_rgb = img.astype(np.uint8)
    def saveImage(img, userId, userName,imgId):
        Path("./dataset/{}".format(userName)).mkdir(parents=True, exist_ok=True)
        cv2.imwrite("./dataset/{}/{}-{}.jpg".format(userName, userId,imgId),img)

    while True:      

        originalImg = new_rgb

        gray_img = cv2.cvtColor(new_rgb, cv2.COLOR_BGR2GRAY)

        faces= faceCascade.detectMultiScale(gray_img, scaleFactor=1.2,minNeighbors=5,minSize=(50,50))

        for(x, y, w, h) in faces:
            cv2.rectangle(new_rgb, (x,y), (x+w, y+h), (0,255,0), 2)
            coords = [x,y,w,h]

        cv2.imshow("identified faces", new_rgb)

        if count<=2:
            roi_img = originalImg[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
            saveImage(roi_img, userId, userName, count)
            count += 1
            time.sleep(2)
        else:
            break
        cv2.destroyAllWindows()
        return train_model(name)

def congrats():
    redirect('\congratulations')

def train_model(name):
    names = []
    paths = []

    for users in os.listdir("dataset"):
        names.append(users)

    for image in os.listdir("dataset/{}".format(name)):
        path_string = os.path.join("dataset/{}/".format(name),image)
        paths.append(path_string)
    faces = []
    ids = []

    print(paths.__len__)
    for img_path in paths:
        print(img_path)
        image = Image.open(img_path).convert("L")
        imgNp = np.array(image,"uint8")
        faces.append(imgNp)
        print(img_path.split("/")[2])
        print(img_path.split("/")[2].split("-")[0])
        id = int(img_path.split("/")[2].split("-")[0])#.split(".")[0])
        ids.append(id)

    ids = np.array(ids)

    trainer = cv2.face.LBPHFaceRecognizer_create()

    trainer.train(faces, ids)

    trainer.write("./training.yml")
    print("get here")
    return render_template('recognize.html')
   
def gen_frames():
    ano="ABC"
    flag=0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("training.yml")

    names = []

    for users in os.listdir("dataset"):
        names.append(users)

    while True:
        success, img = vc.read()
        if not success:
            break
        else:
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            faces= faceCascade.detectMultiScale(gray_img, scaleFactor=1.2,minNeighbors=5,minSize=(50,50))

            for(x, y, w, h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                id, _ = recognizer.predict(gray_img [y:y+h,x:x+w])
                if id:
                    cv2.putText(img, str(id), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1 , cv2.LINE_AA)
                    break
                else:
                    cv2.putText(img, "Unknown", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1 , cv2.LINE_AA)
                    break
            
            cv2.imshow("identified faces", img)
            if 0xFF == ord('q'):
                break
                
        ret, buffer = cv2.imencode('.jpg', img)
        img = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')
    vc.release()
    cv2.destroyAllWindows()

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aadharno = db.Column(db.String(50))
    name = db.Column(db.String(200))
    mail = db.Column(db.String(200))
    phn = db.Column(db.String(200))
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        aadharno = request.form['aadharno']
        name=request.form['name']
        mail=request.form['mail']
        phnno=request.form['phn']
        file = request.files['file']
        upload = Upload(aadharno=aadharno,name=name,mail=mail,phn=phnno,filename=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()
        img=Image.open(file.stream)
        Path("./dataset/{}".format(aadharno)).mkdir(parents=True, exist_ok=True)
        rgb_im = img.convert('RGB')
        rgb_im = rgb_im.save("./dataset/{}/{}".format(aadharno, "image.jpeg"))
        return gen_video(aadharno, name)
    return render_template('img.html')

@app.route('/display/<upload_id>')
def display(upload_id):
    upload = Upload.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=False)    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/videoregistration')
def videoregistration(aadharno, name):
    return Response(gen_video(aadharno, name),mimetype='multipart/x-mixed-replace; boundary=frame')  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        aadharnumber = request.form['aadharno']
        return redirect('recognize')
    return render_template('login.html')

@app.route('/aboutus')
def aboutus():
    return render_template('timeline.html')

@app.route('/recognize')
def recognize():
    return render_template('recognize.html')

@app.route('/videorecognize')
def videorecognize():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame') 
    

@app.route('/congratulations')
def congratulations():
    return render_template('congratulations.html')
    
port = int(os.environ.get("PORT", 5000))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
