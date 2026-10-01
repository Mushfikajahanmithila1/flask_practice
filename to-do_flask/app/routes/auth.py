from flask import render_template, redirect, url_for, Blueprint, flash, request, session

auth = Blueprint("auth", __name__)

User_Credentials = {
    "username": "Mushfikur12",
    "password": "pass23"
}


# Login
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if (
            username == User_Credentials["username"]
            and password == User_Credentials["password"]
        ):
            session["user"] = username
            flash("Login successfully!", "success")

        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")


# Logout
@auth.route("/logout")
def logout():

    session.pop("user", None)
    flash("Logged out.", "info")

    return redirect(url_for("auth.login"))