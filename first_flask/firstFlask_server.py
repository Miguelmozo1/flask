from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("firstFlask_temp.html")

@app.route('/genre')
def blues():
    return render_template("blues.html")

@app.route('/hi/<name>')
def hi(name):
    name_on_temp = name
    return render_template("hi.html", name = name_on_temp)   # name here is used to reference into jinja syntax in html template
    # not needed to make additional html templates, but it does help with organizing the load on one html template

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return f"{num * word}"


if __name__ =="__main__":
    app.run(debug = True, port = 8000)