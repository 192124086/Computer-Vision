import cv2
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
def detect_license_plate(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)    
    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)        
    return frame
video_capture = cv2.VideoCapture("license.mp4")
while True:
    ret, frame = video_capture.read()   
    if not ret:
        break    
    processed_frame = detect_license_plate(frame)   
    cv2.imshow('License Plate Detection', processed_frame)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
