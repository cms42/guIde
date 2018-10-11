# -*- coding: UTF-8 -*-
import sys
import base64
use_cv2=True
dev = False
test_camera=False
camera="/dev/video0"
if len(sys.argv)>1:
    for i in (range(len(sys.argv)-1)):
        if sys.argv[i+1]== '--dev':
            print('您正位于开发者模式')
            dev = True
        elif sys.argv[i+1]=='--no_cv2':
            print('警告：您禁用了cv2')
            use_cv2=False
        elif sys.argv[i+1]=='--test_camera':
            print('将会测试摄像头')
            test_camera=True
        else:
            print('天哪！出错了！未知命令行：',sys.argv[i+1])
if not dev:
    from xugu import *
else:
    from xugu_dev import *
if use_cv2:
    import cv2
if test_camera:
    import numpy
    import matplotlib.pyplot as plot
    cap = cv2.VideoCapture(0)
    #print(cap.isOpened())
    while(1):
        _,frame = cap.read()
        #print(frame)
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

from aip import AipFace
client = AipFace('14381359',  'P0yGUXYuoAfslBDZhisKk0v6','fhmUxqSEAvPUl4DEM4Fzt3aj8G3ybmTb')
