<<<<<<< HEAD
# Social Media Content Analyzer


## Overview
This application analyzes social media content from uploaded PDF or image files and provides engagement improvement suggestions.

## Features
1. File Upload: Supports PDF and image files (PNG, JPG, JPEG) with drag-and-drop interface
2. Text Extraction: 
   - PDF parsing using PyPDF2
   - OCR for images using Tesseract
3. Content Analysis: Basic metrics and improvement suggestions

## Installation
1. Install Python 3.8+
2. Install Tesseract OCR
3. Clone repository
4. Run `pip install -r requirements.txt`
5. Run `python app.py`

## Usage
1. Start the application
2. Open browser to `http://localhost:5000`
3. Drag and drop or select a file
4. Click "Analyze" to see results

## Technical Details
- Framework: Flask
- PDF Processing: PyPDF2
- OCR: Tesseract via pytesseract
- Image Processing: Pillow

## Limitations
- Basic analysis only
- Single file upload at a time
- Simple error handling




SocialMediaAnalyzer/
├── static/
|  ├── css/
│   │   └── style.css
│   └── uploads/
├── templates/
│   ├── index.html
│   └── result.html
├── app.py
├── requirements.txt
└── README.md
=======
# Social Media Content Analyzer

## Overview
This application analyzes social media content from uploaded PDF or image files and provides engagement improvement suggestions.

## Features
1. File Upload: Supports PDF and image files (PNG, JPG, JPEG) with drag-and-drop interface
2. Text Extraction: 
   - PDF parsing using PyPDF2
   - OCR for images using Tesseract
3. Content Analysis: Basic metrics and improvement suggestions

## Installation
1. Install Python 3.8+
2. Install Tesseract OCR
3. Clone repository
4. Run `pip install -r requirements.txt`
5. Run `python app.py`

## Usage
1. Start the application
2. Open browser to `http://localhost:5000`
3. Drag and drop or select a file
4. Click "Analyze" to see results

## Technical Details
- Framework: Flask
- PDF Processing: PyPDF2
- OCR: Tesseract via pytesseract
- Image Processing: Pillow

## Limitations
- Basic analysis only
- Single file upload at a time
- Simple error handling
>>>>>>> master
