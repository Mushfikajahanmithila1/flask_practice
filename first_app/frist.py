from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def home():
    return "You are in the home page."

@app.route("/about")
def about():
    return "You are in the about page."

@app.route("/contact")
def contact():
    return "You are in the contact page."

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.methods == "POST":
        return "You send data."
    else: 
        return "You are just viewing."