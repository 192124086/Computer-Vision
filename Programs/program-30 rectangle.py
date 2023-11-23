import numpy as np
import cv2
def rectangle_image():
    img_size = int(input("Enter the image size: "))
    img = np.ones((img_size, img_size, 3), dtype=np.uint8) * 255  
    x = 50
    y = 50
    width = 200
    height = 100
    color = (0, 0, 255) 
    cv2.rectangle(img, (x, y), (x + width, y + height), color, -1)  
    cv2.imshow('Rectangle Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
rectangle_image()
