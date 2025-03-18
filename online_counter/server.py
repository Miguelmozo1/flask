from flask_app import app
from flask import render_template, session, redirect, request

@app.route("/")
def index():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("counter.html")



@app.route("/add_one")
def add_one():
    if "counter" not in session:
        session["counter"] = 0
    else:
        return redirect("/")


@app.route("/add_two")
def add_two():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return redirect("/")

@app.route("/increment", methods=["POST"])
def add_increment():
    number = request.form["increment"]
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += int(number) - 1
    return redirect("/")



@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True, port = 8000)