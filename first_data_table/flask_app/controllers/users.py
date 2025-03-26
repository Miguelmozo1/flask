from flask import render_template
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("first_data_table.html", users = User.get_all())