import cv2
import numpy as np

# # cap = cv2.VideoCapture("Reasources/test_video.mp4")
# # 0 because its the first webcamer
cap = cv2.VideoCapture(0)
# width is id number 3, lenght is id number 4
cap.set(3, 640)
cap.set(4, 480)
# 10 is brightness
cap.set(10, 100)



while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
