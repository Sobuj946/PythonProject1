import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()

while True:
    _,frame=cap.read()
    cv2.imshow('Virtual Mouse',frame)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    cv2.waitKey(1)