from flask_app import app
from flask_app.controllers import simple_survey

if __name__ == "__main__":
    app.run(port = 8000, debug = True )