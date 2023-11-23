import cv2
def detect_corners(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    corners_threshold = 0.01 * corners.max()
    corner_image = image.copy()
    corner_image[corners > corners_threshold] = [0, 0, 255]  
    return corner_image

image_path = "cam.jpeg"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Error: Could not read the image.")
else:
    corner_detected_image = detect_corners(original_image)
    cv2.imshow("Corner Detected Image", corner_detected_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
