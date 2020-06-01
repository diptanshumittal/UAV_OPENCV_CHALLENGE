import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np 
img1 = cv2.imread('hist.jpg')
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
plt.hist(img.ravel(),256,[0,256])
plt.show()
equ = cv2.equalizeHist(img)
plt.hist(equ.ravel(),256,[0,256])
plt.show()
# adaptive contrast
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
plt.hist(equ.ravel(),256,[0,256])
plt.show()
res = np.hstack((img, equ)) 
cv2.imshow('image', res)
cv2.imshow('i',img1)
cv2.imshow('clahe',cl1)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
