import cv2  
import numpy as np


vi = cv2.VideoCapture(0)



while(True):    
    ret,frame = vi.read()  
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) 
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC) 
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO) 
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th4 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


    cv2.imshow('Binary Threshold Inverted', thresh2) 
    cv2.imshow('Truncated Threshold', thresh3) 
    cv2.imshow('Set to 0', thresh4) 
    cv2.imshow('Set to 0 Inverted', thresh5)
    cv2.imshow('frame', frame)
    cv2.imshow('frame1', th2)
    cv2.imshow('frame2', th3)
    cv2.imshow('frame3', th4)
    cv2.imshow('Binary Threshold', thresh1)
    if cv2.waitKey(1) & 0xff == ord('q'):
        vi.release()
        cv2.destroyAllWindows()




# Binary Threshold with the otsu binarization
#gaussian adaptive with otsu binarization
#Binary threshold inverted
