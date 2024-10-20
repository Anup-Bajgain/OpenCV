import mediapipe as mp
import cv2 as cv
import os

output_dir ="./output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
image_link = os.path.abspath("person.jpg")
img = cv.imread(image_link)

H,W,_=img.shape
mp_face_detection=mp.solutions.face_detection
with mp_face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5) as face_detection:
    img_rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    if out.detections is not None:
        for detection in out.detections:
            location_data=detection.location_data
            bbox=location_data.relative_bounding_box

            x1,y1,w,h = bbox.xmin,bbox.ymin,bbox.width,bbox.height
            y1=int(H*y1)
            x1=int(W*x1)
            w=int(W*w)
            h=int(H*h)

            # cv.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),3)
            img[y1:y1+h,x1:x1+w,:] = cv.blur(img[y1:y1+h,x1:x1+w, :],(50,50))

cv.imwrite(os.path.join(output_dir,"blured_face.png"),img)

# face = cv.VideoCapture(0)

# while True:
#     ret,frame=face.read()
#     cv.imshow("Frame",frame)
#     if cv.waitKey(1) & 0xFF==ord("d"):
#         break
# face.release()
# cv.destroyAllWindows() 
