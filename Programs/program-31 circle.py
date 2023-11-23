import numpy as np
import cv2
def circle_image():
    img_size = int(input("Enter the image size: "))
    img = np.ones((img_size, img_size, 3), dtype=np.uint8) * 255  
    center_x = img_size // 2
    center_y = img_size // 2
    radius = min(img_size // 4, img_size // 5) 
    color = (255,0,0)  
    cv2.circle(img, (center_x, center_y), radius, color, -1)  
    cv2.imshow('Circle Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
circle_image()
