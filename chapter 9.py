import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
handCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_hand.xml")
# img = cv2.imread("Reasources/lena.png")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#
# for (x,y,w,h) in faces:
#     cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

# cv2.imshow("Result", img)
# cv2.waitKey(0)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# 10 is brightness
cap.set(10, 100)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    hands = handCascade.detectMultiScale(imgGray, 1.1, 2)
    eyes = eyeCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # for (x, y, w, h) in eyes:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #
    # for (x, y, w, h) in hands:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
