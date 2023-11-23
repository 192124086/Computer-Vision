import cv2
import numpy as np
def subtract_foreground(image, lower_color, upper_color):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    foreground = cv2.bitwise_and(image, image, mask=mask)
    return foreground
if __name__ == "__main__":
    input_image = cv2.imread("anushka.jpeg")
    lower_color = np.array([0, 0, 100])
    upper_color = np.array([180, 255, 255]) 
    result = subtract_foreground(input_image, lower_color, upper_color)
    cv2.imshow("Original Image", input_image)
    cv2.imshow("Subtracted Foreground", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
