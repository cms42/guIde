#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:12:41 2018

@author: james
"""

import cv2
import requests
import json
import threading
import time
import base64
import numpy as np

access_token="24.24131eaf14f56d7ea563646f09d7d19a.2592000.1541851973.282335-14381359"
face_num=0
frame=None
now_time=0

def b64_to_cvimg(b64):
    try:
        imgData = base64.b64decode(b64)
        nparr = np.frombuffer(imgData, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        return "error"

def cvimg_to_b64(img):
    try:
        image = cv2.imencode('.jpg', img)[1]
        base64_data = str(base64.b64encode(image))[2:-1]
        return base64_data
    except Exception as e:
        return "error"


def get_face_info(img64):
    url="https://aip.baidubce.com/rest/2.0/face/v3/search"
    url = url + "?access_token=" + access_token
#    data = {"image_type":"BASE64",
#            "group_id_list":group_id,
#            "image":img,
#            "max_user_num":user_top_num,
#            "liveness_control":"NORMAL"}
    data={"company_id":"10000",
          "access_token":access_token,
          "img":img64}
    try:
        response = requests.post(url,files=None,data=data)
        res_text=response.text
        res_json=json.loads(res_text)
        return res_json
    except Exception:
        return "error"
    
def post_request(frame,face_num,nt):
    if(face_num>0) and (time.time()-nt>3):
        global now_time
        now_time=time.time()
        #print(now_time)
        img64=cvimg_to_b64(frame)
        res=get_face_info(img64)
        try:
            print(str(res["result"]["face_list"][0]["gender"]),str(res["result"]["face_list"][0]["beauty"]))
        except Exception:
            pass
        time.sleep(3)

def faceDetect(img,face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')):
    size=img.shape[:2]
    divisor = 8
    h,w=size
    minSize=(w//divisor,h//divisor)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 2,cv2.CASCADE_SCALE_IMAGE,minSize)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    return img,len(faces)

def main():
    cap = cv2.VideoCapture(0)
    global now_time
    now_time=time.time()
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #frame = imread("2017-02-26-200818.jpg")
        # Our operations on the frame come here
        if ret == True:
            frame1,face_num = faceDetect(frame)
            t=threading.Thread(target=post_request,args=(frame,face_num,now_time,), name='POST_REQUEST')
            t.start()
            
        # Display the resulting frame
        cv2.imshow('frame',frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

main()
