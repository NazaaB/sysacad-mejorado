from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .facultad import Facultad


db = SQLAlchemy()

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sysacad.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    return app

