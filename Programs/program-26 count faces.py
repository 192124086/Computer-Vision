import cv2
img = cv2.imread("face.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
num_faces = len(faces)
print(f"Number of faces detected: {num_faces}")
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Faces Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
