from flask import Flask, render_template
from post import Post


app = Flask(__name__)
data = Post()
num_len = len(data.title)


@app.route("/")
def home():
    return render_template(
        "index.html",
        title=data.title,
        subtitle=data.subtitle,
        body=data.body,
        num_len=num_len,
    )


@app.route("/post/<num>")
def get_blog(num):
    i = int(num)
    return render_template(
        "post.html", title=data.title[i], subtitle=data.subtitle[i], body=data.body[i]
    )


if __name__ == "__main__":
    app.run(debug=True)
