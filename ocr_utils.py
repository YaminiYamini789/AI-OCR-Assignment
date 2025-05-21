import pytesseract
from pdf2image import convert_from_path
import cv2
import tempfile

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    results = []
    for page in images:
        with tempfile.NamedTemporaryFile(suffix='.png') as temp:
            page.save(temp.name)
            img = cv2.imread(temp.name)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
            text = pytesseract.image_to_string(thresh)
            results.append(text)
    return "\n".join(results)
