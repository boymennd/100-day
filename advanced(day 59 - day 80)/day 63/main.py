from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(230), unique=True, nullable=False)
    author = db.Column(db.String(230), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


db.create_all()


@app.route("/")
def home():
    books = db.session.query(Book).all()
    return render_template("index.html", books=books)


@app.route("/delete")
def delete():
    book_id = request.args.get("num")
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["name"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/id=<int:num>", methods=["GET", "POST"])
def change(num):
    book = Book.query.get(int(num))
    if request.method == "POST":
        book.rating = request.form["rate"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template(
        "change.html", name=book.title, rating=book.rating
    )


if __name__ == "__main__":
    app.run(debug=True)
