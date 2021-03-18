from flask import Flask
import random

app = Flask(__name__)

num = random.randint(1, 9)


@app.route("/")
def hello():
    return (
        "<h1 style='color:red;text-align:center;'>Choose number (1 to 9 )!</h1>"
        "<img style='display:block;margin-left:auto;margin-right:auto;' "
        "src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif'>"
    )


@app.route("/<choose>")
def number(choose):
    if int(choose) == num:
        return (
            f"<h1 style='color:green;text-align:center'>You right the num is {num}</h1>"
            "<img style='display:block;margin-left:auto;margin-right:auto;' "
            "src='https://media.giphy.com/media/3o7bu4G19uhzAf1DYQ/giphy.gif'>"
        )
    elif int(choose) > num:
        return (
            f"<h1 style='color:yellow;text-align:center'>Too high try again !</h1>"
            "<img style='display:block;margin-left:auto;margin-right:auto;'"
            " src='https://media.giphy.com/media/79eQOjPPrisR9B2zy6/giphy.gif'>"
        )
    else:
        return (
            f"<h1 style='color:blue;text-align:center'>Too low try again !!</h1>"
            "<img style='display:block;margin-left:auto;margin-right:auto;'"
            " src='https://media.giphy.com/media/XJLEXP9xEJRevqXxnR/giphy.gif'>"
        )


if __name__ == "__main__":
    app.run(debug=True)
