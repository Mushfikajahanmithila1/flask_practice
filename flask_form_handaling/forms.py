from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("Enter your full name", validators=[DataRequired(message="Enter a valid name")])
    email = StringField("Enter your email", validators=[DataRequired("Enter a email"), Email("Email dosen't exits")])
    password = PasswordField("Enter your password", validators=[DataRequired("Give a password"), Length(min=8)])
    submit = SubmitField("Register")