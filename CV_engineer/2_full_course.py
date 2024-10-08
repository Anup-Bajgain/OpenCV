import cv2 as cv
import os
import numpy as np

#reading image
# image_link = os.path.abspath("cars.jpg")
# # print(image_link)
# img = cv.imread(image_link)
# print(type(img))
# cv.imshow("cars",img)
# cv.waitKey(0)


#reading videos
# video_path = os.path.abspath('video12.mp4')
# video = cv.VideoCapture(0)
# while True:
#     isFrame, frame = video.read()
#     edge = cv.Canny(frame,100,200) #just for fun
#     cv.imshow("frame by frame",frame)
#     cv.imshow("lines",edge)
#     if cv.waitKey(1) & 0xFF == ord("b"):
#         # i=i+1
#         # cv.imwrite(f"image_{i}.jpg",frame)
#         break
# video.release()
# cv.destroyAllWindows()


#resizing
# rs = cv.resize(img, (190,1080)) #values can be anything i.e greater or lesser than original value
# w,h,d=img.shape
# print(w,h,d,type(w))
# print(img.shape)
# print(rs.shape)
# cv.imshow("resized image",rs)
# cv.imshow("cars",img)
# cv.waitKey(0)


#cropping
# cropped = img[200:600,100:500]
# cv.imshow("cropped",cropped)
# cv.waitKey(0)


#colourspaces
# image_link = os.path.abspath("OIP.jpg")
# img = cv.imread(image_link)
# # print(img.shape)
# rs = cv.resize(img, (298*3,180*3))
# # cv.imshow("bird",img)
# coloured = cv.cvtColor(rs,cv.COLOR_BGR2RGB)
# gray = cv.cvtColor(rs,cv.COLOR_BGR2GRAY)
# hsv = cv.cvtColor(rs,cv.COLOR_BGR2HSV)
# cv.imshow("BGR bird",rs)
# cv.imshow("hsv bird",hsv)
# # cv.imshow("RGB bird",coloured)
# # cv.imshow("gray bird",gray)
# cv.waitKey(0)


#Blurring
# image_link = os.path.abspath("person.jpg")
# img = cv.imread(image_link)
# k_size =7
# # bl = cv.blur(img, (k_size,k_size)) #normal blur
# # bl = cv.GaussianBlur(img,(k_size,k_size),3) 
# bl = cv.medianBlur(img,k_size)
# cv.imshow("not blurred",img)
# cv.imshow("blurred",bl)
# cv.waitKey(0)

#Image threshold
# image_link = os.path.abspath("person.jpg")
# img = cv.imread(image_link)
# bl=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ret,thresh =cv.threshold(bl,100,255,cv.THRESH_BINARY)
# cv.imshow("modified",bl)
# cv.imshow("modified_2",thresh)
# cv.imshow("Normal",img)
# cv.waitKey(0)


#edge detection
# image_link = os.path.abspath("basketball_play.jpg")
# img = cv.imread(image_link)
# edge = cv.Canny(img,100,200)
# dilate = cv.dilate(edge,np.ones((1,1),dtype =np.int8)) #erode can be used to erode the thick lines
# cv.imshow("not blurred",img)
# cv.imshow("edge detection",edge)
# cv.imshow("edge detection bold",dilate)
# cv.waitKey(0)


#drawing
# image_link = os.path.abspath("basketball_play.jpg")
# img = cv.imread(image_link)
# #line
# cv.line(img,(100,150),(300,450),(0,255,0),3)
# #rectangle
# cv.rectangle(img,(100,150),(300,450),(230,28,89),2)
# #text
# cv.putText(img, "hey\n There",(200,350), cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
# #circle
# cv.circle(img,(200,350),100,(222,111,0),2)

# cv.imshow("not blurred",img)
# # cv.imshow("edge detection",line)
# # cv.imshow("edge detection bold",dilate)
# cv.waitKey(0)


###contours
image_link = os.path.abspath("birds.jpg")
img = cv.imread(image_link)
img =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(img,100,255,cv.THRESH_BINARY_INV)
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# print(contours,hierarchy)
for cnt in contours:
    if cv.contourArea(cnt)>100:
        x1,y1,w,h=cv.boundingRect(cnt)
        cv.rectangle(img,(x1,y1),(x1+w,y1+h),(0,0,255),1)
cv.imshow("not Normal",thresh)
cv.imshow("Normal",img)
cv.waitKey(0)

# #boiler code
# image_link = os.path.abspath("person.jpg")
# img = cv.imread(image_link)


# cv.imshow("Normal",img)
# cv.waitKey(0)