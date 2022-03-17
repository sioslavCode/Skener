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
    form = PictureForm()
    
    if request.method == "POST":
        ocr = SadrzajForm()
        image = Image.open(ocr)
        text = pytesseract.image_to_string(image)
        return render_template("home.html", title="title", korisnik="Sio", metoda=metoda, form=form)
    else:
        text = pytesseract.image_to_string(image)
        metoda = "GET"
        return render_template("home.html", title="title", korisnik="Sio", metoda=metoda, form=form, ocr=text)


class PictureForm(FlaskForm):
    picture = FileField('Select document')
    submit = SubmitField('Submit')

class SadrzajForm(FlaskForm):
    sadrzaj= TextAreaField("Teksst")
