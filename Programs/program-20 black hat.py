import cv2
import numpy as np

image_path = "dora.png"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)
closed_image = cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, kernel)
black_hat_image = cv2.subtract(closed_image, original_image)

cv2.imshow("Original Image", original_image)
cv2.imshow("Closed Image", closed_image)
cv2.imshow("Black Hat Image", black_hat_image)

