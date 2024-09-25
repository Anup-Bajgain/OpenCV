from djitellopy import Tello
import cv2
t = Tello()
t.connect()
t.takeoff()
t.land()