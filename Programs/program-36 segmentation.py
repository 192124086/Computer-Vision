import cv2
def on_trackbar(val):
    _, thresholded = cv2.threshold(src_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow("Result", thresholded)
src = cv2.imread("eyes.jpeg", cv2.IMREAD_COLOR)
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.imshow("Original", src)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Threshold", "Result", 0, 255, on_trackbar)
on_trackbar(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
