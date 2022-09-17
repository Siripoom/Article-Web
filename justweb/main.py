

from msilib.schema import MsiAssemblyName
from unicodedata import name
from flask import Flask, render_template , request
from flask_wtf import FlaskForm
from wtforms import TelField, SubmitField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'


class Myform(FlaskForm):
    name = TelField("Enter your name.")
    submit = SubmitField("Submit")


@app.route("/")
def index():
    articletitle = ["What is Flask Python","What is a Web Framework?",
    "What is Flask?", "WSGI", "Werkzeug", "jinja2", "Microframework", "Why is Flask a good web framework choice? "]
    return render_template("index.html",articletitle = articletitle)

@app.route("/about")
def about ():
    return render_template("about.html")

@app.route("/admin")
def profile():
    # name ส่งค่าไปยัง template
    username = "Moopiris"
    return render_template("admin.html",myname = username) # ใช้ paramiter = ตัวแปรที่เก็บค่าที่ต้องการส่งไป
# @app.route("/user/<name>/<age>")
# def member(name, age):
#     return "<center><h2>Firstname : {} , Age : {}</h2></center>".format(name,age)
@app.route("/sended")
def contact():
    name = request.args.get('fname')
    description = request.args.get('description')
    return render_template("thank.html",data={"name": name,"description":description})

@app.route("/form",methods=['GET','POST'])
def forms():
    name = False
    form = Myform()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("Form_wtf.html",form=form,name=name)


if __name__ == "__main__":
    app.run(debug=True)    #can use debug mode type "debug=true" in bracketsc