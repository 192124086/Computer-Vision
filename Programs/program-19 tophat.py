import cv2
import numpy as np
image_path = "group.jpeg"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

opened_image = cv2.morphologyEx(original_image, cv2.MORPH_OPEN, kernel)
top_hat_image = cv2.subtract(original_image, opened_image)
cv2.imshow("Original Image", original_image)
cv2.imshow("Opened Image", opened_image)
cv2.imshow("Top Hat Image", top_hat_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
