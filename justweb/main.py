
from flask import Flask, render_template , request,session
from flask_wtf import FlaskForm
from wtforms import TelField, SubmitField, BooleanField,RadioField,SelectField,TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class Myform(FlaskForm):
    name = TelField("Enter your name.",validators=[DataRequired()])
    isAccept = BooleanField("Accept condition")
    submit = SubmitField("Submit")
    career = SelectField('career',choices=[('Programer','Programer'),('Developer','Dev'),('Game Dev','Game Dev')])
    gender = RadioField('sex',choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    message = TextAreaField("Enter your message")
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
    form = Myform()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['career']  = form.career.data
        session['message'] = form.message.data
        #clear data
        form.message.data = ""
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.career.data = ""
    return render_template("Form_wtf.html",form=form,)


if __name__ == "__main__":
    app.run(debug=True)    #can use debug mode type "debug=true" in bracketsc