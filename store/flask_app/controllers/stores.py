from flask_app import app
from flask import render_template, request, redirect, session, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/checkout", methods=["POST"])
def checkout():
    print(request.form)
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["student_id"] = request.form["student_id"]
    session["strawberry"] = request.form["strawberry"]
    session["raspberry"] = request.form["raspberry"]
    session["apple"] = request.form["apple"]
    print(f"Charging {session["first_name"]} for {int(session["strawberry"])+ int(session["raspberry"]) + int(session["apple"])} fruits")
    return render_template("checkout.html")

@app.route("/products")
def products():
    return render_template("products.html")