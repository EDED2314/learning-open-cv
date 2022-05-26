import cv2
import numpy as np

# joining images xd i think i nkow how to do that hm

img = cv2.imread("Reasources/lena.png")

# horizontal stack
imgHor = np.hstack((img, img))

# vertical stack
imgVer = np.vstack((img,img))

# both of them need the same channels and size and width and - bruh the person did not show how to fricking code it D:

cv2.imshow("Horizontal", imgHor)
cv2.imshow('vertical', imgVer)


cv2.waitKey(0)