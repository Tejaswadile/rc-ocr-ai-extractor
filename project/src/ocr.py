import pytesseract

from src.preprocessing import preprocess_image


def extract_text(image_path):
    processed_image = preprocess_image(image_path)
    config = "--oem 3 --psm 6"
    return pytesseract.image_to_string(processed_image, config=config)
