import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# width is id number 3, lenght is id number 4
cap.set(3, 640)
cap.set(4, 480)
# 10 is brightness
cap.set(10, 150)
#  blue, yellow red
myColors = [[89, 179, 123, 255, 164, 255], [16, 179, 78, 255, 182, 255],
            [24, 179, 133, 255, 143, 255]]
myColorValues = [[255, 0, 0], [51, 255, 255], [255, 51, 51]]

myPoints = [[]]

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        h_min = color[0]
        sat_min = color[2]
        val_min = color[4]
        h_max = color[1]
        sat_max = color[3]
        val_max = color[5]

        lower = np.array([h_min, sat_min, val_min])
        upper = np.array([h_max, sat_max, val_max])
        # mask would filter out and filter out the image without that color
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints
        # cv2.imshow(str(color[0]), mask)



def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for ct in contours:
        area = cv2.contourArea(ct)
        if area > 500:
            # cv2.drawContours(imgResult, ct, -1, (250, 0, 0), 3)
            peri = cv2.arcLength(ct, True)
            approx = cv2.approxPolyDP(ct, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return (x + w // 2, y)

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        if len(point) != 0:
            cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newpoint in newPoints:
            myPoints.append(newpoint)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
