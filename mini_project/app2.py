from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    # if username == "Mushfikur1" and password == "pass":
    #     return render_template("welcome.html", name = username)
    valid_users = {
        "admin" : "123",
        "Mushfikur1" : "pass",
        "Mushfika1" : "pass34"
    }
    if username in valid_users and password in valid_users[username]:
        return render_template("welcome.html", name = username)
    else:
        return "Invalid credentials. Try again."
