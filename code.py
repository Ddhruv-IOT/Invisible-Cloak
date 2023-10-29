#This a python program which works as invisibility cloak
#It uses opencv and numpy libraries and a webcam to make the invisibility cloak work
#Now it can only make a black cloak but you can change the color by changing the values of lower_black and upper_black

import cv2
import numpy as np
import time

# Display an introduction message
print("Harry: Hey! Would you like to try my invisibility cloak?\nIt's awesome!\nPrepare to get invisible...")

# Initialize the video capture object
cap = cv2.VideoCapture(0)
time.sleep(2)

# Capture and store the background frame for later use
background = None
for _ in range(30):
    _, background = cap.read()

# Flip the background frame horizontally for consistent alignment
background = np.flip(background, axis=1)

# Continuously process video frames
while cap.isOpened():
    # Capture the current frame from the camera
    ret, img = cap.read()
    if not ret:
        break

    # Flip the current frame horizontally for consistent alignment
    img = np.flip(img, axis=1)

    # Convert the current frame to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the black color range in the HSV color space
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 30])

    # Create masks for black color detection
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Apply morphological operations (opening) to the mask to remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    # Replace pixels in the current frame corresponding to the "cloak" with background pixels
    img[np.where(mask == 255)] = background[np.where(mask == 255)]

    # Display the resulting frame
    cv2.imshow('Invisibility Cloak', img)

    # Check for the "Esc" key (ASCII code 27) to exit the loop
    k = cv2.waitKey(10)
    if k == 27:
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
