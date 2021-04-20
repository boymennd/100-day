from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
import smtplib, os

pass_mail = os.environ.get("PASS_MAIL")
mail = "iobi1907@gmail.com"
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        meg = request.form["meg"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=mail, password=pass_mail)
            connection.sendmail(
                from_addr=mail,
                to_addrs=mail,
                msg=f"Subject:New contact\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Message: {meg}",
            )
        return render_template("success.html", name=name)
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
