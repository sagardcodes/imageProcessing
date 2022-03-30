#median filter
import cv2

# read the image
image = cv2.imread("b.png", 0)

# apply the 3x3 median filter on the image
processed_image = cv2.medianBlur(image, 3)
# display image
cv2.imshow('Median Filter Processing Sagar Dahal ', processed_image)
# save image to disk
cv2.imwrite('processed_image.png', processed_image)
cv2.waitKey(0)
