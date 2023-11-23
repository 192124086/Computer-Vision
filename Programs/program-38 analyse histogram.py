import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(image_path)
    b, g, r = cv2.split(img)
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
    plt.figure(figsize=(10, 6))
    plt.plot(hist_b, color='blue', label='Blue')
    plt.plot(hist_g, color='green', label='Green')
    plt.plot(hist_r, color='red', label='Red')
    plt.title('Color Histogram Analysis')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
image_path = "anushka.jpg"
analyze_histogram(image_path)
