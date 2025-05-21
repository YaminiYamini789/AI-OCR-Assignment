from fastapi import FastAPI, UploadFile, File
from ocr_utils import extract_text_from_pdf
from parse_results import parse_lab_results, generate_summary

app = FastAPI()

@app.post("/upload-report")
async def upload_report(file: UploadFile = File(...)):
    with open("temp.pdf", "wb") as f:
        f.write(await file.read())
    text = extract_text_from_pdf("temp.pdf")
    results = parse_lab_results(text)
    summary = generate_summary(results)
    return {"structured_data": results, "summary": summary}
