import cv2
import numpy as np

img_1 = cv2.imread('broken.jpg', 0) / 255  # convert each pixel value to range of {0-255}
gamma = 3
img_2 = np.power(img_1, gamma)

gamma = 5
img_3 = np.power(img_1, gamma)
cv2.imshow("original", img_1)
cv2.imshow("gamma 3Sagar Dahal", img_2)
cv2.imshow("gamma 5", img_3)
cv2.waitKey(1000000000)
