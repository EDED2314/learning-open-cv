import cv2
import numpy as np

# i think pygame is coded off cv2 :flushed:

# import matplotlib.pyplot as plt

# all black image if we are using a 2 level mimage
img = np.zeros((512,512, 3))
# height width
# print(img.shape)
# whole img is (255, 0, 0) BGR, so its blue
# height width
# img[200:300, 100:512] = 255, 0, 0

# starting point, ending point, color (B, G, R), thikness
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# starting point, ending point, color (B, G, R), thikness, it is not filled if cv2.FILLED is not put in the para
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 2, cv2.FILLED)
# cetner point, radius,  color (B, G, R), thikness, it is not filled if cv2.FILLED is not put in the para
cv2.circle(img, (450, 50), 30, (255, 255, 0), 5)
# the image, text, origin where we want to start it (width, height) (x is eastm y is south), font, scale (size ig), color BGR, thik
cv2.putText(img, "OPENCV ", (300, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 150, 0), 3)


cv2.imshow("image", img)

cv2.waitKey(0)