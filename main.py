from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    name="anchal"
    #here name is from python file and nm is from sublime template file..
    return render_template("about.html",nm=name)

app.run()