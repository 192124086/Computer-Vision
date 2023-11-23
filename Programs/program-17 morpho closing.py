import cv2
import numpy as np

image_path = "jerry.png"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

closed_image = cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original Image", original_image)
cv2.imshow("Closed Image", closed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
