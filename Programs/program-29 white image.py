import numpy as np
import cv2
def color_box():
    img_size = int(input("Enter the image size: "))
    box_size = int(img_size / 10)
    img = np.ones((img_size, img_size, 3));  
    img[:box_size, :box_size] = (0, 0, 0)  
    img[:box_size, -box_size:] = (1, 0, 0) 
    img[-box_size:, :box_size] = (0, 1, 0) 
    img[-box_size:, -box_size:] = (0, 0, 1) 
    cv2.imshow('Colored Boxes Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
color_box()
