#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("../xugu")
sys.path.append("../share")
sys.path.append("./")

from aip import AipFace
from aip import AipSpeech
import base64
import cv2
import numpy as np
import json

class face_sync:
    def __init__(self,config):
        APP_ID = config["APP_ID"]
        API_KEY = config["API_KEY"]
        SECRET_KEY = config["SECRET_KEY"]
        self.client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    def b64_to_cvimg(self,b64):
        try:
            imgData = base64.b64decode(b64)
            nparr = np.frombuffer(imgData, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            return img
        except Exception as e:
            return "error",e
    def cvimg_to_b64(self,img):
        try:
            image = cv2.imencode('.jpg', img)[1]
            base64_data = str(base64.b64encode(image))[2:-1]
            return base64_data
        except Exception as e:
            return "error",e
    def search_b64img(self,img,groupIdList):
        imageType="BASE64"
        return self.client.search(img, imageType, groupIdList)
    def search_cvimg(self,img,groupIdList):
        return self.search_b64img(self.cvimg_to_b64(img),groupIdList)

class speech_sync:
    class AipSpeechError(Exception):
        """
        无效参数错误
        """
        pass

    def __init__(self,config):
        APP_ID = config["APP_ID"]
        API_KEY = config["API_KEY"]
        SECRET_KEY = config["SECRET_KEY"]
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
