from flask import Flask, render_template
import datetime, requests

app = Flask(__name__)
agify_api = "https://api.agify.io"
gender_api = "https://api.genderize.io"


def gender_get(name):
    parameters = {"name": name}
    response = requests.get(url=gender_api, params=parameters)
    return response.json()["gender"]


def agify_get(name):
    parameters = {"name": name}
    response = requests.get(url=agify_api, params=parameters)
    return response.json()["age"]


@app.route("/")
def hello():
    return "<h1 style='text-align:center;'>Please choose name in the link !</h1>"


@app.route("/guess/<name>")
def guess_name(name):
    date = datetime.datetime.now().year
    return render_template(
        "index.html", date=date, name=name, age=agify_get(name), gender=gender_get(name)
    )


if __name__ == "__main__":
    app.run(debug=True)
