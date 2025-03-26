from flask_app import app
from flask import render_template, request, session, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user")
def show_user():
    return render_template("user.html")


@app.route("/submit", methods=["POST"])
def save_user():
    session["name"] = request.form["name"]
    session["fav_lang"] = request.form["fav_lang"]
    session["description"] = request.form["description"]
    return redirect("/user")