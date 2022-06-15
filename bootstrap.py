import routes as routes
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/http://techmeideas'
db = SQLAlchemy(app)


    # srno name phon_num msg date email
class Contact(db.Model):

      srno = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(80), nullable=False)
      phon_num = db.Column(db.String(12), nullable=False)
      msg = db.Column(db.String(120), nullable=False)
      date = db.Column(db.String(12),  nullable=False)
      email = db.Column(db.String(20), nullable=False)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/Contact',methods=['GET','POST'])
def Contact():
    if (request.method== 'POST'):

        name= request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        message=request.form.get("message")
        return render_template("contact.html")

entry= Contact(name= name,phone_num=phone,msg=message,email= email)
db.session.add(entry)
db.session.commit()
app.run(debug=True)