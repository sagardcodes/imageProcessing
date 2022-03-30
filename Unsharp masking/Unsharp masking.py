#unsharp masking
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage.filters import median_filter
import numpy as np

original_image = plt.imread("abc.png").astype('uint16')

# Convert to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Median filtering
gray_image_mf = median_filter(gray_image, 1)

# Calculate the Laplacian
lap = cv2.Laplacian(gray_image_mf, cv2.CV_64F)

# Calculate the sharpened image
#sharp = gray_image - 0.7 * lap

cv2.imshow("Sharpened image sagar", original_image)
cv2.waitKey(0)
