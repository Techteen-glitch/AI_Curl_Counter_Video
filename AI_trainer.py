import cv2
import mediapipe as mp
import numpy as np
import time
import Module as pm
cap=cv2.VideoCapture('Blueshirt.mp4')
detector=pm.poseDetector()
dir=0
pTime=0
count=0
while True:
    success, img=cap.read()  
    img = cv2.resize(img, (1280, 720))
    #img=cv2.imread('Image.jpg')
    img=detector.findPose(img, False)
    lmList=detector.findPosition(img, False)
    #print(lmList)
    if len(lmList)!=0:
        #Right
        #detector.findAngle(img, 12,14,16)
        #Left
        angle=detector.findAngle(img, 11,13,15)
        per=np.interp(angle, (200, 330), (0, 100))
        bar=np.interp(angle, (200, 330), (650, 100))
        colour=(255, 0, 0)
        if per==100:
            colour=(0, 255, 0)
            if dir==0:
                count+=0.5
                dir=1
        if per==0:
            colour=(0, 255, 0)
            if dir==1:
                count+=0.5
                dir=0
        print(count)
    cv2.rectangle(img, (1100, 100), (1175, 650), colour,3)
    cv2.rectangle(img, (1100, int(bar)), (1175, 650), colour, cv2.FILLED)
    cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 3, colour, 3)
    cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15, (255, 0, 0), 5)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.imshow('Image', img)
    cv2.waitKey(1)