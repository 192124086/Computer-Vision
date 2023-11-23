import cv2
img = cv2.imread('face.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt_tree.xml')
faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2)

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Detected faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
