import cv2
import numpy as np
def subtract_background(image_path, threshold=100):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    background_removed = cv2.bitwise_and(img, img, mask=mask_inv) 
    return background_removed
image ="cam.jpeg"
result = subtract_background(image)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
