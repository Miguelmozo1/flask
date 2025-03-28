from flask_app import app
from flask import render_template, redirect, session, request
import random

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process_money():
    session["gold"] = session["gold"]
    if request.form["building"] == "farm":
        session["gold"] += random.randint(10,20)
    if request.form["building"] == "cave":
        session["gold"] += random.randint(5,10)
    if request.form["building"] == "house":
        session["gold"] += random.randint(2,5)
    if request.form["building"] == "casino":
        session["gold"] += random.randint(-50,50)
    return redirect("/")


@app.route("/clear")
def restart():
    session.clear()
    return redirect("/")