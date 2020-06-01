import cv2 
import numpy as np
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)    
while(1):
    l=0
    _, frame = cap.read()

    img_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    frame = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,70])
    upper_red = np.array([0,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    #lower_red = np.array([30,150,100])
    #upper_red = np.array([255,255,185])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask=mask1+mask2
    mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
    mask2 = cv2.bitwise_not(mask1) 
    res = cv2.bitwise_and(frame,frame, mask= mask1) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask)
    cv2.imshow('mask1',mask1)
    cv2.imshow('mask2',mask2) 
    cv2.imshow('res',res)
    cv2.imshow('hue',hsv)
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
cv2.destroyAllWindows() 
cap.release()


  


    
