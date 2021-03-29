from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators

import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)
COFFEE_RATING = ["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
WIFI_RATING = ["💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
POWER_RATING = ["🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]


class CafeForm(FlaskForm):
    name = StringField("Cafe name", validators=[validators.DataRequired()])
    url = StringField(
        "Location URL", validators=[validators.URL("That is not valid a url address")]
    )
    open = StringField("Open time", validators=[validators.DataRequired()])
    close = StringField("Closing time", validators=[validators.DataRequired()])
    coffee = SelectField("Coffee rating", choices=COFFEE_RATING)
    wifi = SelectField("Wifi strength rating", choices=WIFI_RATING)
    power = SelectField("Power socket availability", choices=POWER_RATING)
    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    data = (
        form.name.data,
        form.url.data,
        form.open.data,
        form.close.data,
        form.coffee.data,
        form.wifi.data,
        form.power.data,
    )
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", newline="", encoding="utf8") as f:
            writer = csv.writer(f)
            writer.writerow(data)
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
