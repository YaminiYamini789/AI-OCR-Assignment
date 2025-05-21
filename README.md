# AI-OCR-Assignment
AI OCR Assignment
Overview
This project performs OCR on scanned medical PDFs, extracts lab test results, and provides a summary.

Setup
Install dependencies:
pip install fastapi uvicorn pytesseract pdf2image opencv-python
sudo apt install tesseract-ocr
Run the app:
uvicorn main:app --reload
Usage
Use Postman to POST a PDF file to http://127.0.0.1:8000/upload-report

Output
Returns structured test results and a rule-based medical summary.
