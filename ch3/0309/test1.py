import sys 
import numpy as np
import cv2

#배경 동영상 로드
cap2 = cv2.VideoCapture("raining.mp4")
if not cap2.isOpened():
    print('video open failed!')
    sys.exit()
    
#녹색 배경 동영상 로드
cap1 = cv2.VideoCapture('woman.mp4') #괄호안에 0이면 노트북 캠으로 대체

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()