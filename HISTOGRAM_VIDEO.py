import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import time

vi = cv2.VideoCapture(0)
fig,ax = plt.subplots(1,1)
ax.set_xlim([0,256])
fig.show()

while(1):
    ax.clear()
    _, frame = vi.read()
    for i, col in enumerate(['b' , 'g' , 'r']):
        hist = cv2.calcHist([frame] , [i] , None ,[256], [0, 256])
        ax.plot(hist , color=col) 
    fig.canvas.draw()
    time.sleep(1)        

cv2.waitKey(0) 
cv2.destroyAllWindows() 
