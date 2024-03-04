from flask_app import app
from flask import render_template, request, redirect, session
import random



@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "activities" not in session:
        session["activities"] = []
    return render_template("index.html")

@app.route("/process/gold", methods = ["POST"])
def gold():
    session["gold"] = session["gold"]
    if request.form["job"] == "pan":
        int = random.randint(0,3)
        session["gold"] += int
        session["activities"].append(int)
    if request.form["job"] == "pickaxe":
        int = random.randint(3,10)
        session["gold"] += int
        session["activities"].append(int)
    if request.form["job"] == "gamble":
        int = random.randint(-35,25)
        session["gold"] += int
        session["activities"].append(int)
    if request.form["job"] == "mine":
        int = random.randint(-60,40)
        session["gold"] += int
        session["activities"].append(int)
    return redirect("/")

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")