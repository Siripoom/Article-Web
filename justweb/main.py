from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about ():
    return render_template("about.html")

@app.route("/admin")
def profile():
    return render_template("admin.html")

# @app.route("/user/<name>/<age>")
# def member(name, age):
#     return "<center><h2>Firstname : {} , Age : {}</h2></center>".format(name,age)

if __name__ == "__main__":
    app.run()    #can use debug mode type "debug=true" in brackets