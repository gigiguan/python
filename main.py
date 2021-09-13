# import "packages" from flask
from flask import Flask, render_template
from flask import request

# create a Flask instance
app = Flask(__name__)


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
            return render_template("gigi.html", name=name)
    # starting and empty input default
    return render_template("gigi.html", name="World")


@app.route('/jessie', methods=['GET', 'POST'])
def jessie():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("jessie.html", name=name)
    # starting and empty input default
    return render_template("jessie.html", name="World")


@app.route('/Neha/')
def stub():
    return render_template("Neha.html")


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Neha.html", name=name)
    # starting and empty input default
    return render_template("Neha.html", name="How's your day?")


@app.route('/shruti/', methods=['GET', 'POST'])
def shruti():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("shruti.html", name1=name)
    # starting and empty input default
    return render_template("shruti.html", name1="World")

@app.route('/mini_labs', methods=['GET', 'POST'])
def mini_labs():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("mini_labs.html", name=name)
    # starting and empty input default
    return render_template("mini_labs.html", name="World")

@app.route('/theme/')
def theme():
    return render_template("theme.html")

@app.route('/binary/')
def binary():
    return render_template("binary.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
