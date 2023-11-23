import cv2
import numpy as np
path="tree.jpeg"
img=cv2.imread(path)
if img is None:
    print("Error")
else:
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imggray,(7,7),0)
    cv2.imshow("Image Blur",imgblur)
    cv2.waitKey(0)
    



