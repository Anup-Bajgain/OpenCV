import mediapipe as mp
import cv2 as cv
import os
import argparse

def process_img(img,face_detection):
    H,W,_=img.shape
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

            if x1 >= 0 and y1 >= 0 and x1 + w <= img.shape[1] and y1 + h <= img.shape[0]:
            # Apply blur to the ROI
                img[y1:y1+h, x1:x1+w, :] = cv.blur(img[y1:y1+h, x1:x1+w, :], (50, 50))
            else:
                print("Warning: Invalid region of interest detected.")
    return img
            
output_dir ="./output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
image_link = os.path.abspath("video_1.mp4")
img = cv.imread(image_link)

mp_face_detection=mp.solutions.face_detection

args=argparse.ArgumentParser()
args.add_argument('--mode',default='video')
args.add_argument('--filePath',default=image_link)
args = args.parse_args()

with mp_face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5) as face_detection:
    if args.mode in ['image']:
        img = cv.imread(args.filePath)

        img = process_img(img,face_detection)
    elif args.mode in ['video']:
        
        cap = cv.VideoCapture(0)
        ret,frame=cap.read()
        output_video = cv.VideoWriter(os.path.join(output_dir,"output.mp4"),cv.VideoWriter_fourcc(*'MP4V'),24,(frame.shape[1],frame.shape[0]))
        while ret:
            frame =process_img(frame,face_detection)
            cv.imshow("blurred",frame)
            output_video.write(frame)
            ret,frame=cap.read()
            if cv.waitKey(1) & 0xFF == ord("b"):
                break
        cap.release()
        cv.destroyAllWindows()
# cv.imwrite(os.path.join(output_dir,"blured_face.png"),img)
