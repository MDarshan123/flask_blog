from flask import Flask,render_template
app=Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello world"

# @app.route("/Ds")
# def ds():
#     return "Hello Darshan23"

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    name="dsmalaviya"
    return render_template("about.html",name2=name)

app.run(debug=True)