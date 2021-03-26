from flask import Flask, render_template, request
import requests, smtplib, os

response = requests.get("https://api.npoint.io/e39ae88a65c74519165a").json()
MY_MAIL = "iobi1907@gmail.com"
PASS = os.environ.get("PASS_MAIL")
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


@app.route("/contact", methods=["POST"])
def contact1():
    if request.method == "POST":
        name = request.form["name"]
        phone_number = request.form["phone_number"]
        email = request.form["email"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASS)
            connection.sendmail(
                from_addr=MY_MAIL,
                to_addrs=MY_MAIL,
                msg=f"Subject: New commenet\n\nName: {name}\n"
                f"Phone_number: {phone_number}\n"
                f"Email: {email}\n"
                f"Message:\n{message}",
            )
        return render_template("success.html", name=name)

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
