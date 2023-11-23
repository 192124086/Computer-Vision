import cv2

def resize_image(image, scale_factor):
    # Calculate the new dimensions
    new_width = int(image.shape[1] * scale_factor)
    new_height = int(image.shape[0] * scale_factor)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    return resized_image

# Read the image
image_path = "apple.jpg"
original_image = cv2.imread(image_path)

if original_image is None:
    print("Error: Could not read the image.")
else:
    # Resize the image to a bigger size
    bigger_image = resize_image(original_image, scale_factor=2.0)

    # Resize the image to a smaller size
    smaller_image = resize_image(original_image, scale_factor=0.5)

    # Display the original, bigger, and smaller images
    cv2.imshow("Bigger Image", bigger_image)
    cv2.imshow("Smaller Image", smaller_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
