import cv2 as cv
import os

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
#     cv.imshow("frame by frame",frame)
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
image_link = os.path.abspath("OIP.jpg")
img = cv.imread(image_link)
blurred = cv.blur()
cv.waitKey(0)