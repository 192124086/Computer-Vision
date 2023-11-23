import cv2
image_path = "group2.jpeg"
img = cv2.imread(image_path)
converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Original Image (BGR)", img)
cv2.imshow("Converted Image (HSV)", converted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
