from fastapi import FastAPI, File, UploadFile, HTTPException
import pdfplumber
import pytesseract
from PIL import Image, UnidentifiedImageError
import io

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file uploaded")
        
        contents = await file.read()
        
        if file.filename.lower().endswith(".pdf"):
            text = extract_text_from_pdf(contents)
        elif file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
            text = extract_text_from_image(contents)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        if not text:
            raise HTTPException(status_code=400, detail="No text extracted")
        
        return {"filename": file.filename, "extracted_text": text}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


def extract_text_from_pdf(pdf_bytes):
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF processing error: {str(e)}")
    return text.strip()


def extract_text_from_image(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Invalid image format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR processing error: {str(e)}")
    return text.strip()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
