from flask_app import app
from flask_app.controllers import game

if __name__ == "__main__":
    app.run(debug = True, port = 8000)