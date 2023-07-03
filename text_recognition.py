import cv2
import pytesseract

def recognize_text(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Preprocess the image (optional)
    # Apply image processing techniques like resizing, cropping, or enhancing

    # Perform text recognition using pytesseract
    recognized_text = pytesseract.image_to_string(image)

    return recognized_text
