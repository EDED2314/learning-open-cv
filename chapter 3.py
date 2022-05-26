import cv2
import numpy as np


img = cv2.imread("Reasources/lena.png")
print(img.shape)
# (512, 512, 3) this array it is height width and then the amount of planes e.g. its 3 if its BGR or RBG

imgResize = cv2.resize(img, (412, 412))
print(imgResize.shape)

imgIncrease = cv2.resize(img, (600, 600))

# every iamge is a matrix
# height comes first height then width because row then col
# we are keeping upper half since the display is x east, y south, then we are keeping the middle of the x
imgCropped = img[0:200, 200:500]

# cv2.imshow("Image Increased", imgIncrease)
cv2.imshow("Image Cropped", imgCropped)
cv2.imshow("Image", img)
# cv2.imshow("Image Resized", imgResize)
cv2.waitKey(0)