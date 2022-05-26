import cv2
import numpy as np

# detecting certain colors

def empty(a):
    return

path = 'Reasources/lena.png'
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 512, 512)
# val in normall color, then saturation changes the light
# name, the img, value that starts; count is somethign werid, it goes up to 360 but open cv offers to 180; call a functions everytime when the trackbar chanegs
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
# the count goes to 255
cv2.createTrackbar("Sat Min", "Trackbars", 133, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 143, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

cap = cv2.VideoCapture(0)
# width is id number 3, lenght is id number 4
cap.set(3, 640)
cap.set(4, 480)
# 10 is brightness
cap.set(10, 100)
while True:
    success, img = cap.read()



    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    sat_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    sat_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    val_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    val_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    # hsv is humindity, saturation and value for that color range??
    print(h_min,h_max, sat_min, sat_max, val_min, val_max)

    # time for some colors? creating mask in the range of the colors
    # img, the lower limit, uper limit, the mins and maxs
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    # mask would filter out and filter out the image without that color
    mask = cv2.inRange(imgHSV, lower, upper)

    # now that we have these values, we put these as our initial values

    # now we get the  iamge in the colors from the mask
    # adds the images, bitwise add??? then it clips it ig, leanered it in class xd
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Video", img)
    cv2.imshow("mask", mask)
    cv2.imshow("result", imgResult)
    # cv2.imshow("img hsv", imgHSV)
    # cv2.imshow("Original", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break