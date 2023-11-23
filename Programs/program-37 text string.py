import cv2 
path = "Dq.jpeg" 
image = cv2.imread(path) 
window_name = 'Image'
font = cv2.FONT_HERSHEY_SIMPLEX 
org = (50, 50) 
fontScale = 1
color = (0, 0, 255) 
thickness = 2
image = cv2.putText(image, 'Dq', org, font, fontScale, color, thickness, cv2.LINE_AA) 
cv2.imshow(window_name, image) 
