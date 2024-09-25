import cv2 as cv

#reading image
# img = cv.imread("D:\Media\Pictures\Facebook\FB_IMG_16064471120632781.jpg")
# cv.imshow("me",img)

#reading videos
capture = cv.VideoCapture(0)
#integer value for cameras
#path reads  the video of that path

i=1
while True:
    
    isTrue, frame = capture.read()
    cv.imshow(f"frame_by_frame{i}",frame)
    if cv.waitKey(20) & 0xFF==ord("o"):
        break
    i++1
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)