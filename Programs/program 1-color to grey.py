import cv2
import numpy as np
path="apple.jpg"
img=cv2.imread(path)
if img is None:
    print("Error")
else:
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScale",imggray)
    cv2.waitKey(0)


