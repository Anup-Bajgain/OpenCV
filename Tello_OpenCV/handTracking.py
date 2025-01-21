import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    if not success:
        break
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_img)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            # Get the coordinates of the index fingertip (landmark 8)
            fingertip_x, fingertip_y = int(hand_landmarks.landmark[8].x * ws), int(hand_landmarks.landmark[8].y * hs)
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            direction = ""
            if fingertip_x < ws // 3:
                direction = "Left"
            elif fingertip_x > 2 * ws // 3:
                direction = "Right"
            
            if fingertip_y < hs // 3:
                direction += " Up"
            elif fingertip_y > 2 * hs // 3:
                direction += " Down"

            cv2.putText(img, f"Direction: {direction}", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

            # Draw a circle around the fingertip to highlight its position
            cv2.circle(img, (fingertip_x, fingertip_y), 10, (0, 0, 255), cv2.FILLED)

    else:
        cv2.putText(img, "No Hand Detected", (400, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
