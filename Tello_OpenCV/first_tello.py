
from djitellopy import Tello
import cv2
import time

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

# Fly in different directions
tello.move_up(50)  # Move up by 50 cm
tello.move_forward(50)  # Move forward by 100 cm
tello.move_back(50)  # Move back by 50 cm
tello.move_left(50)  # Move left by 50 cm
tello.move_right(50)  # Move right by 50 cm
tello.rotate_clockwise(90)  # Rotate 90 degrees clockwise
tello.rotate_counter_clockwise(90)  # Rotate 90 degrees counterclockwise
while True:
    # Get a frame from the Tello camera
    frame = tello.get_frame_read().frame

    # Show the frame using OpenCV
    cv2.imshow("Tello Video Feed", frame)

    # Optionally, you can add hand tracking or other drone controls here

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Hover for a moment
time.sleep(2)

# Land the drone
tello.land()

# Close the connection
tello.end()



# # Initialize Tello drone
# tello = Tello()

# # Connect to Tello
# tello.connect()

# # Check battery percentage
# battery = tello.get_battery()
# print(f"Battery: {battery}%")

# # Start video streaming
# tello.streamon()

# # Take off
# tello.takeoff()

# # Main loop for handling video feed
# while True:
#     # Get a frame from the Tello camera
#     frame = tello.get_frame_read().frame

#     # Show the frame using OpenCV
#     cv2.imshow("Tello Video Feed", frame)

#     # Optionally, you can add hand tracking or other drone controls here

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Land the drone
# tello.land()

# # Close the connection and release resources
# tello.streamoff()  # Stop video streaming
# cv2.destroyAllWindows()
