from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/e39ae88a65c74519165a").json()

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", all_posts=response)


@app.route("/post/<int:i>")
def post(i):
    num = i - 1
    return render_template(
        "post.html",
        title=response[num]["title"],
        body=response[num]["body"],
        subtitle=response[num]["subtitle"],
        date=response[num]["date"],
        author=response[num]["author"],
        image_url=response[num]["image_url"],
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
