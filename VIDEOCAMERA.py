import numpy as np
import cv2

vi = cv2.VideoCapture(0)


while(True):
    ret, frame = vi.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vi.release()
cv2.destroyAllWindows()
