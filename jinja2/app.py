from flask import Flask, render_template, request, redirect, url_for, Response

app = Flask(__name__)
@app.route("/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        valid_users = {
                "admin" : "123",
                "Mushfikur1" : "pass",
                "Mushfika1" : "pass34"
            }
        if username in valid_users and password == valid_users[username]:
                return render_template("home.html")
        else:
            return Response("Invalid creadintial. Try again.", mimetype="text/plain")
    else:
        return render_template("login2.html")

@app.route("/submit", methods = ["POST", "GET"])
def submit():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")