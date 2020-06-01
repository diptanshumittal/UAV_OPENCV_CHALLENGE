import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('DSC_0176.jpg')
img = cv2.resize(img,(360,480))


img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
for i, col in enumerate(['b' , 'g' , 'r']):
    hist = cv2.calcHist(img , [i] , None ,[256], [0, 256])
    plt.plot(hist , color=col)
plt.show()
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
for i, col in enumerate(['b' , 'g' , 'r']):
    hist = cv2.calcHist(img_output , [i] , None ,[256], [0, 256])
    plt.plot(hist , color=col)
plt.show()


cv2.imshow('Color input image', img)
cv2.imshow('Histogram equalized', img_output)

cv2.waitKey(0)
