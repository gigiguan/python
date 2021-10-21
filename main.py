# import "packages" from flask
import requests
from flask import Flask, render_template
from flask import request
from image import image_data
from api.webapi import api_bp
from starter.starter import app_starter

from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f


# create a Flask instance
app = Flask(__name__)
app.register_blueprint(app_starter)
app.register_blueprint(api_bp)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gigi', methods=['GET', 'POST'])
def gigi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("ABOUT/gigi.html", name=name)
    # starting and empty input default
    return render_template("ABOUT/gigi.html", name="World")

@app.route('/jessie', methods=['GET', 'POST'])
def jessie():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("ABOUT/jessie.html", name=name)
    # starting and empty input default
    return render_template("ABOUT/jessie.html", name="World")


@app.route('/Neha/')
def stub():
    return render_template("ABOUT/Neha.html")


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("ABOUT/Neha.html", name=name)
    # starting and empty input default
    return render_template("ABOUT/Neha.html", name="How's your day?")


@app.route('/shruti/', methods=['GET', 'POST'])
def shruti():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("ABOUT/shruti.html", name1=name)
    # starting and empty input default
    return render_template("ABOUT/shruti.html", name1="World")

@app.route('/mini_labs', methods=['GET', 'POST'])
def mini_labs():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("MINI_LABS/mini_labs.html", name=name)
    # starting and empty input default
    return render_template("MINI_LABS/mini_labs.html", name="World")

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    BITS=8
    imgBulbOn = "static/assets/openbook.jpg"
    if request.form:
        BITS = int(request.form.get("BITS"))
        imgBulbOn = request.form['lightOn']
    return render_template("MINI_LABS/binary.html", imgBulbOn=imgBulbOn, BITS=BITS)

@app.route('/apush/')
def apush():
    return render_template("HISTORY/apush.html")

@app.route('/apel/')
def apel():
    return render_template("ENGLISH/apel.html")

@app.route('/aplit/')
def aplit():
    return render_template("ENGLISH/aplit.html")

@app.route('/apbio/')
def apbio():
    return render_template("SCIENCE/apbio.html")

@app.route('/apgov/')
def apgov():
    return render_template("HISTORY/apgov.html")

@app.route('/apeuro/')
def apeuro():
    return render_template("HISTORY/apeuro.html")

@app.route('/RGB/')
def RGB():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('MINI_LABS/RGB.html', images=image_data(path))

@app.route('/Logic Gates/')
def Logicgates():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('MINI_LABS/Logicgates.html', images=image_data(path))


@app.route('/unsigned addition/', methods=['GET', 'POST'])
def unsigned_addition():
    return render_template("MINI_LABS/unsigned addition.html", BITS=8, imageOn="/static/assets/openbook.jpg", imageOff="/static/assets/closedbook.jpg")

@app.route('/signed addition/', methods=['GET', 'POST'])
def signed_addition():
    return render_template("MINI_LABS/signed addition.html", BITS=8, imageOn="/static/assets/openbook.jpg", imageOff="/static/assets/closedbook.jpg")



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
