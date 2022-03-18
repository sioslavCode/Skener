from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField, TextAreaField
import pytesseract
from PIL import Image

app = Flask(__name__)
app.secret_key = b'_5#y2Lg"F4Qdawd8z\n\xec]/'


@app.route('/', methods=["GET", "POST"])
@app.route('/home')
def home():
    text = ""
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/file.png')
        text = pytesseract.image_to_string(Image.open(f))

    return render_template("home.html", text=text)
