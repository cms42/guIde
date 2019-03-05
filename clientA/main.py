#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
sys.path.append("../xugu")
sys.path.append("../share")

from face import face_sync
from net import net_client_sync
import json
import cv2.cv2 as cv2
import threading
import base64
import numpy as np
import time

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

def post_request(frame,nt):
    if (time.time()-nt>3):
        global now_time
        now_time=time.time()
        #print(now_time)
        fc=face_sync(config["face"])
        res=fc.search_cvimg(frame,{0})
        try:
            #print(str(res))
            if res['error_code']==0:
                if res['error_msg']=='SUCCESS':
                    result = res['result']
                    #print(str(result))
                    for face in result['user_list']:
                        if face['score'] >=60.0:
                            print('Face looks OK!')
                            print('group id:',face['group_id'],'user id:',face['user_id'])
                            print('score:',face['score'])
                            nc=net_client_sync()
                            nc.post_request(("127.0.0.1",9999),face['group_id']+face['user_id'])
                        else:
                            print('ERROR:score<60')
                            print(res)
                else:
                    print('ERROR:error_msg<>"SUCCESS"')
                    print(res)
            else:
                print('ERROR:error_code<>0')
                print(res)
        except Exception:
            pass
        time.sleep(3)

if __name__ == "__main__":
    if len(sys.argv)<2:
        config_name="config.json"
    else:
        config_name=sys.argv[2]
    config=json.load(open(config_name,'r'))
    cap = cv2.VideoCapture(0)
    global now_time
    now_time=time.time()
    while(True):
        ret, frame = cap.read()
        if ret == True:
            frame1,face_num = faceDetect(frame)
            if(face_num>0):
                t=threading.Thread(target=post_request,args=(frame,now_time,), name='POST_REQUEST')
                t.start()
        cv2.imshow('frame',frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
