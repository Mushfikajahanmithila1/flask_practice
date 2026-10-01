from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createApp():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqllite:///site.db'
    db.init_app(app)
    return app