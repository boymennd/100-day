from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app
app = create_app()
app.config["SECRET_KEY"] = "congxp1996"
USER_NAME= "boymennd"
PASSWORD = "congxp1996"

class MyForm(FlaskForm):
    name = StringField(
        "Username",
        [validators.InputRequired("This username is required"),
         validators.Length(min=4,message="username must be more 4 char")
         ])
    password = PasswordField(
        "Password",
        [
            validators.InputRequired("THis password is required"),
            validators.Length(min=8, max=50, message="Little short for password"),
        ],
    )
    email = StringField(
        "Email",
        [
            validators.Length(min=6, message=("Little short for an email address?")),
            validators.Email(message="That's not a valid email address.")

        ],
    )
    submit = SubmitField("Submit")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.name.data == USER_NAME and form.password.data == PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)
