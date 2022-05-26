import cv2
import numpy as np

img = cv2.imread("Reasources/lena.png")
# cvt color chages everythign to gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 0)
imgCanny = cv2.Canny(img, 150, 200)

'''
Dilation adds pixels to the boundaries of objects in an image, while erosion removes 
pixels on object boundaries. The number of pixels added or 
removed from the objects in an image depends on the size and shape of 
the structuring element used to process the image.
'''

kernel = np.ones((5,5), np.float32)
# i think this is for thickness and blur ig (thickness only if we are using the sides (img canny))
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2. imshow("Canny Image", imgCanny)
cv2. imshow("Dilation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
# cv2. imshow("Blur Image", imgBlur)
# cv2. imshow("Gray Image", imgGray)
cv2.waitKey(0)
