import requests
from flask import Blueprint, render_template

app_starter = Blueprint('starter', __name__,
                        url_prefix='/starter',
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='assets')


@app_starter.route('/joke', methods=['GET', 'POST'])
def joke():

    url = "http://127.0.0.1:5000/api/joke"
    response = requests.request("GET", url)
    return render_template("starter/joke.html", joke=response.json())


@app_starter.route('/jokes', methods=['GET', 'POST'])
def jokes():

    url = "http://127.0.0.1:5000/api/jokes"

    response = requests.request("GET", url)
    return render_template("starter/jokes.html", jokes=response.json())


