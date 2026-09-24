from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def profile():
    return render_template(
    "profile.html",
    name="Mushfikur",
    is_topper=True,
    subjects=["Math", "Science", "Programming"]
)
