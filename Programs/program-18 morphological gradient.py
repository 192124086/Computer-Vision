import cv2
import numpy as np
image_path = "doremon.jpeg"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)
gradient_image = cv2.morphologyEx(original_image, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Original Image", original_image)
cv2.imshow("Morphological Gradient", gradient_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

