from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("boxes.html")

@app.route('/<int:x>/')
def select(x):
    return render_template("xboxes.html", num = x)


@app.route('/<int:x>/<color>')
def colors(x, color):
    return render_template("coloredBoxes.html", num =x, color = color)


if __name__ == "__main__":
    app.run(debug = True, port = 8000)