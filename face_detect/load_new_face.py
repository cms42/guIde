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
#access_token="24.081c1804cdb7b78c3aeec57a4018ae87.2592000.1541994040.282335-14381359"
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


def upload_face(img64,uid,group_id,user_info):
    url="https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
    url = url + "?access_token=" + access_token
#    data = {"image_type":"BASE64",
#            "group_id_list":group_id,
#            "image":img,
#            "max_user_num":user_top_num,
#            "liveness_control":"NORMAL"}
#    data={"company_id":"10000",
#          "access_token":access_token,
#          "img":img64}
    data={
                 "image_type":"BASE64",
                 "image":img64,
                 "user_id":uid,
                 "group_id":group_id,
                 "user_info":user_info
    }
    headers={'content-type': 'application/x-www-form-urlencoded'}
    try:
        #response = requests.post(url,files=None,data=data)
        response = requests.post(url,data=data,headers=headers)
        res_text=response.text
        res_json=json.loads(res_text)
        return res_json
    except Exception:
        return "error"
    time.sleep(1)
    
def post_request(frame,uid,group_id,user_info):
        img64=cvimg_to_b64(frame)
        res=upload_face(img64,uid,group_id,user_info)
        try:
            print(str(res))
            if res['error_code']==0:
                if res['error_msg']=='SUCCESS':
                    result = res['result']
                    #print(str(result))
                    
        except Exception:
            pass

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
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.waitKey(1) & 0xFF == ord('s'):
                print('import your group:')
                group_id= input()
                print('import your name:')
                uid = input()
                print('import your user info:')
                user_info = input()
                post_request(frame,uid,group_id,user_info)
            
        # Display the resulting frame

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

main()
