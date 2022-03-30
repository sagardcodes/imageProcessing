#mean filter
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('b.png',0)
cv2.imshow(' Sagar Grey scale',img)
blur = cv2.blur(img, (5, 5))


# display image
#cv2.imshow('Mean Filter Processing Sagar Dahal',blur)
# save image to disk
cv2.imwrite(' Sagar  mean processed_image .png ', blur)
# pause the execution of the script until a key on the keyboard is pressed
cv2.waitKey(0)
