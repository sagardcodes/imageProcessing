#histogram equalization

import cv2
import numpy as np
from matplotlib import pyplot as plt

# histogram plotting  of original image
img = cv2.imread('before histogram equalization.jpg', 0)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# histogram equalization result
equ = cv2.equalizeHist(img)
plt.hist(equ.ravel(), 256, [0, 256])
plt.show()
res = np.hstack((img, equ))  # stacking images side-by-side
cv2.imshow('res', equ)
cv2.waitKey(1000000)
