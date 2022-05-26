import cv2
import numpy as np

path = 'Reasources/shapes.jpg'
img = cv2.imread(path)


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for ct in contours:
        area = cv2.contourArea(ct)
        # print(area)
        # real imgae, contour, then all or all?, color in BGR, then thiknbes
        if area>500:
            cv2.drawContours(imgContour, ct, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(ct, True)
            # the contour, resolution (can play around a bit with it), then true for closed shape
            approx = cv2.approxPolyDP(ct, 0.02*peri, True)
            # will give us the points of the shapes
            objCor = len(approx)
            print(objCor)
            x,y, w,h = cv2.boundingRect(approx)

            if objCor == 3: object_type = "Tri"
            elif objCor == 4:
                aspect_ratio = w/float(h)
                if aspect_ratio > 0.95 and aspect_ratio < 1.05:
                    # square aspect ratio normally is 1
                    object_type = "Square"
                else:
                    object_type = "Rectangle"
            elif objCor == 5: object_type = "Pentagon"
            elif objCor == 6: object_type = "Hexagon"
            elif objCor == 7: object_type = "Pentagon"
            else: object_type="Circle"

            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(imgContour, object_type,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,0), 2)

    return


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# kernal then sigma or alpha
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgContour = img.copy()
getContours(imgCanny)

# cv2.imshow("orginial", img)
# cv2.imshow('img gray', imgGray)
# cv2.imshow('img blur', imgBlur)
# cv2.imshow('imgg', result)
imgStack = stackImages(1.5, ([img, imgGray, imgBlur], [img, imgContour, imgCanny]))
cv2.imshow("image ", imgStack)
cv2.waitKey(0)
