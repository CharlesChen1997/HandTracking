import numpy as np
import cv2
# import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if ret:
        cv2.imshow('img', img)

    if cv2.waitKey(1) == ord('q'):
        break