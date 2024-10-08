import cv2 as cv
from PIL import Image
import numpy as np

def get_limits(color):
    c=np.uint8([[color]])
    hsvC =cv.cvtColor(c,cv.COLOR_BGR2HSV)
    lower = hsvC[0][0][0]-10,100,100
    upper = hsvC[0][0][0]+10,255,255

    lower =np.array(lower,dtype=np.uint8)
    upper=np.array(upper,dtype=np.uint8)

    return lower,upper



yellow = [0,255,255]
cap = cv.VideoCapture(0)
while True:
    ret,frame =cap.read()
    hsv_image=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower,upper = get_limits(yellow)
    mask =cv.inRange(hsv_image,lower,upper)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()
    if bbox is not None:
        x1,y1,w,b=bbox
        cv.rectangle(frame,(x1,y1),(w,b),(0,255,0),5)

    cv.imshow("Frame",frame)
    if cv.waitKey(1) & 0xFF==ord("d"):
        break
cap.release()
cv.destroyAllWindows() 
