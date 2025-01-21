from djitellopy import Tello
import cv2
import time
import mediapipe as mp
import numpy as np

# Initialize Tello drone
tello = Tello()

# Connect to Tello
tello.connect()

# Get battery percentage
battery = tello.get_battery()
print(f"Battery: {battery}%")
tello.streamon()

# Take off
tello.takeoff()

# Tello video stream address
tello_stream_url = "udp://@0.0.0.0:11111"

# Open the video stream
cap = cv2.VideoCapture(tello_stream_url)

if not cap.isOpened():
    print("Failed to open Tello video stream!")
    exit()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

while True:
    # Get a frame from the Tello camera
    frame = tello.get_frame_read().frame
    ws, hs = frame.shape[1], frame.shape[0]

    # Convert the frame to RGB
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_img)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get the coordinates of the index fingertip (landmark 8)
            fingertip_x, fingertip_y = int(hand_landmarks.landmark[8].x * ws), int(hand_landmarks.landmark[8].y * hs)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            direction = ""
            if fingertip_x < ws // 3:
                direction = "Right"
                tello.move_right(50)
            elif fingertip_x > 2 * ws // 3:
                direction = "Left"
                tello.move_left(50)
            
            if fingertip_y < hs // 3:
                direction += " Up"
                tello.move_up(50)
            elif fingertip_y > 2 * hs // 3:
                direction += " Down"
                tello.move_down(50)

            cv2.putText(frame, f"Direction: {direction}", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

            # Draw a circle around the fingertip to highlight its position
            cv2.circle(frame, (fingertip_x, fingertip_y), 10, (0, 0, 255), cv2.FILLED)

    else:
        cv2.putText(frame, "No Hand Detected", (400, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    
    # Show the frame using OpenCV
    cv2.imshow("Tello Video Feed", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Hover for a moment
time.sleep(2)

# Land the drone
tello.land()

# Close the connection
tello.end()

# Release resources
cv2.destroyAllWindows()