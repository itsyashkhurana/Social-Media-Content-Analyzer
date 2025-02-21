<<<<<<< HEAD

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from flask import Flask, render_template, request, flash
import os
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import re

app = Flask(__name__)
app.secret_key = "supersecretkey"
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error extracting image text: {str(e)}"

def analyze_content(text):
    word_count = len(text.split())
    char_count = len(text)
    hashtag_count = len(re.findall(r'#\w+', text))
    
    suggestions = []
    
    # Existing suggestions...
    if word_count < 20:
        suggestions.append("Consider adding more content (20+ words) for better engagement.")
    if hashtag_count < 2:
        suggestions.append("Add 2-5 relevant hashtags to increase visibility.")
    if hashtag_count > 10:
        suggestions.append("Too many hashtags (10+) may look spammy - reduce to 5-10.")
    
    # Platform-specific length recommendations...
    if char_count > 280:
        suggestions.append("Twitter: Exceeds 280 characters - shorten for better fit.")
    if char_count < 100:
        suggestions.append("Instagram: Posts under 100 characters may lack context - aim for 100-200.")
    if 280 >= char_count > 125:
        suggestions.append("LinkedIn: Ideal length (125-280 chars) for engagement - good job!")
    else:
        suggestions.append("LinkedIn: Aim for 125-280 characters for optimal engagement.")
    
    # Optimal posting times...
    suggestions.append("Twitter: Optimal posting times - 12 PM to 3 PM or 5 PM to 6 PM (local time).")
    suggestions.append("Instagram: Optimal posting times - 11 AM to 2 PM or 6 PM to 9 PM (local time).")
    suggestions.append("LinkedIn: Optimal posting times - 9 AM to 11 AM weekdays (local time).")

    return {
        "word_count": word_count,
        "char_count": char_count,
        "hashtag_count": hashtag_count,
        "suggestions": suggestions
    }

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('index.html')
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return render_template('index.html')
        
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Extract text based on file type
            if filename.lower().endswith('.pdf'):
                text = extract_text_from_pdf(filepath)
            else:
                text = extract_text_from_image(filepath)
            
            # Analyze content
            analysis = analyze_content(text)
            
            return render_template('result.html', 
                                text=text,
                                analysis=analysis,
                                filename=filename)
    
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
=======

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from flask import Flask, render_template, request, flash
import os
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import re

app = Flask(__name__)
app.secret_key = "supersecretkey"
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"

def extract_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error extracting image text: {str(e)}"

def analyze_content(text):
    word_count = len(text.split())
    char_count = len(text)
    hashtag_count = len(re.findall(r'#\w+', text))
    
    suggestions = []
    
    # Existing suggestions...
    if word_count < 20:
        suggestions.append("Consider adding more content (20+ words) for better engagement.")
    if hashtag_count < 2:
        suggestions.append("Add 2-5 relevant hashtags to increase visibility.")
    if hashtag_count > 10:
        suggestions.append("Too many hashtags (10+) may look spammy - reduce to 5-10.")
    
    # Platform-specific length recommendations...
    if char_count > 280:
        suggestions.append("Twitter: Exceeds 280 characters - shorten for better fit.")
    if char_count < 100:
        suggestions.append("Instagram: Posts under 100 characters may lack context - aim for 100-200.")
    if 280 >= char_count > 125:
        suggestions.append("LinkedIn: Ideal length (125-280 chars) for engagement - good job!")
    else:
        suggestions.append("LinkedIn: Aim for 125-280 characters for optimal engagement.")
    
    # Optimal posting times...
    suggestions.append("Twitter: Optimal posting times - 12 PM to 3 PM or 5 PM to 6 PM (local time).")
    suggestions.append("Instagram: Optimal posting times - 11 AM to 2 PM or 6 PM to 9 PM (local time).")
    suggestions.append("LinkedIn: Optimal posting times - 9 AM to 11 AM weekdays (local time).")

    return {
        "word_count": word_count,
        "char_count": char_count,
        "hashtag_count": hashtag_count,
        "suggestions": suggestions
    }

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('index.html')
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return render_template('index.html')
        
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Extract text based on file type
            if filename.lower().endswith('.pdf'):
                text = extract_text_from_pdf(filepath)
            else:
                text = extract_text_from_image(filepath)
            
            # Analyze content
            analysis = analyze_content(text)
            
            return render_template('result.html', 
                                text=text,
                                analysis=analysis,
                                filename=filename)
    
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
>>>>>>> master
    app.run(debug=True)