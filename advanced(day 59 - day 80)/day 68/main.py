from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "any-secret-key-you-choose"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.__init__(app)


@login_manager.user_loader
def user_laod(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


db.create_all()


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    users = User.query.all()
    if request.method == "POST":
        for user in users:
            if user.email == request.form.get("email"):
                flash("The email you entered already exists, please enter it again")
                return redirect(url_for("register"))
        new_user = User(
            email=request.form.get("email"),
            password=generate_password_hash(
                request.form.get("password"), method="pbkdf2:sha256", salt_length=8
            ),
            name=request.form.get("name"),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets", logged_in=current_user.is_authenticated))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    users = User.query.all()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        for user in users:
            if user.email == email:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(
                        url_for("secrets", logged_in=current_user.is_authenticated)
                    )
                else:
                    flash("The password you entered is incorrect")
                    return redirect(url_for("login"))
            else:
                flash("The email you entered is incorrect or does not exist!")
                return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static/files", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
