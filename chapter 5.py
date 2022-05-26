import cv2
import numpy as np

# differnt perspectives (warp persepctives)

img = cv2.imread("Reasources/lena.png")
# in the tutorial they are using cards, the plain card is width = 2.5 inch and length is 3.5 inch
width, height = 250, 350

# we first declere the 4 points  of which shape you want to warpo persepcgive
pts1 = np.float32([[111,219], [287, 188], [154, 482], [352, 440]])

# the width and ehight of the frame
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
# width height again??? D:
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Imgae", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)