import cv2

def detect_eyes(image_path):
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=1, minSize=(30, 30))
    for (x, y, w, h) in eyes:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Eye Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "dq.jpg"
    detect_eyes(image_path)
