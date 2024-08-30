import cv2
import dlib
import numpy as np
import os
import time


feed = cv2.VideoCapture(0)


landmark_file ="shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(landmark_file)

while True:
    ret, frame = feed.read()
    if cv2.waitKey(1) == ord("q") or ret == False:
        break
    else:
        frame = cv2.flip(frame, 1)
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image_shape = frame.shape

        cv2.imshow("", frame)

        faces = detector(gray_img, 0)

        for face in faces:
            landmarks = predictor(gray_img, face)

                


feed.release()
cv2.destroyAllWindows()