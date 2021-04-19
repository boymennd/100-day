from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap

CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    "-": "---...",
    " ": "/",
    "=": "-...-",
    "+": ".-.-.",
    "_": "..--.-",
}
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)
list_change = []
text_output = None
text_start = None


def word_to_morse(text):
    list_not = []
    for char in text:
        if char.upper() in CODE:
            list_change.append(CODE[char.upper()])
        else:
            list_not.append(char)
    if len(list_not) == 0:
        return " ".join(list_change)
    else:
        return f"Can't encode: {' '.join(list_not)}"


def more_to_word(text):
    list_word = []
    list_morse = text.split()
    for item in list_morse:
        for char in CODE:
            if CODE[char] == item:
                list_word.append(char)
                list_morse.remove(item)
    if len(list_morse) == 0:
        return "".join(list_word)
    else:
        return f"Can't decode : {''.join(list_morse)}"


@app.route("/")
def home():
    return render_template("index.html", text_start=None, text="anh cong")


@app.route("/encode", methods=["GET", "POST"])
def encode():
    global text_output, text_start
    if request.method == "POST":
        text = request.form["text"]
        text_output = word_to_morse(text)
        text_start = text
        return redirect(url_for("encode", text_start=text, text=text_output))
    return render_template("index.html", text_start=text_start, text=text_output)


@app.route("/decode", methods=["GET", "POST"])
def decode():
    global text_output, text_start
    if request.method == "POST":
        text = request.form["text"]
        text_start = text
        text_output = more_to_word(text)
        return redirect(url_for("decode", text_start=text_start, text=text_output))
    return render_template("index.html", text_start=text_start, text=text_output)


if __name__ == "__main__":
    app.run(debug=True)
