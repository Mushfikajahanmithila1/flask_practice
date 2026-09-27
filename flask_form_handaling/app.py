from flask import Flask, flash, redirect, render_template, request, url_for
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "my-secrect_key"

@app.route("/", methods=["GET", "POST"])  
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    name = form.name.data
    email = form.email.data
    flash(f"Welcome, {name}! You Registered Successfully!", "success")
    return redirect(url_for("success"))  
  return render_template("register.html", form=form)

@app.route("/success")
def success():
  return render_template("success.html")

app.config["WTF_CSRF_ENABLED"] = True













# @app.route("/", methods=["GET", "POST"])
# def form():
#   if request.method == "POST":
#     name = request.form.get("name")
#     if not name:
#       flash("Name could not be empty")
#       return redirect(url_for("form"))

#     flash(f"Thank you {name}. Your feedback was saved")
#   # Jodi thank you page-e name dekhte chao, tahole query parameter ba session use korte paro.
#     return redirect(url_for("thankyou", name=name))

#   # GET request er jonno eta ensure korte hobe:
#   return render_template("form.html")

# @app.route("/thankyou")
# def thankyou():
#   # URL theke name-ti grab kore template-e pass korchi
#   name = request.args.get("name")
#   return render_template("thankyou.html", name=name)