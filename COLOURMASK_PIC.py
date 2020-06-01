import cv2 
import numpy as np
img = cv2.imread('red1.jpg')
l=0 ;
print(l)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
for i in range(len(img)) :
    print(i)
    for j in range(len(img[i])):
        l+=1
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
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
res = cv2.bitwise_and(img,img, mask= mask1) 
cv2.imshow('frame',img)  
cv2.imshow('res',res)



  


    
