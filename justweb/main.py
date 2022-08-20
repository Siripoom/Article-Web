from msilib.schema import MsiAssemblyName
from unicodedata import name
from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run()    #can use debug mode type "debug=true" in brackets