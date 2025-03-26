from flask_app import app
from flask import render_template, session, request, redirect
import random


@app.route("/")
def index():
    session["random"] = random.randint(1,100)
    print(session["random"])
    session["attempt"] = 0
    print(session["attempt"])
    return render_template("number_game.html")

@app.route("/attempt", methods = ["POST"])
def attempts():
    session["attempt"] += 1
    if session["attempt"] == 5:
        return redirect("/lose")
    if int(session["random"]) == int(request.form["attempt"]):
        return redirect("/equal")
    if int(session["random"]) < int(request.form["attempt"]):
        return redirect("/too_high")
    else:
        return redirect("/too_low")


@app.route("/equal")
def equal():
    return render_template("equal.html")

@app.route("/too_high")
def too_high():
    return render_template("too_high.html")

@app.route("/too_low")
def too_low():
    return render_template("too_low.html")

@app.route("/lose")
def lose():
    return render_template("lose.html")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")