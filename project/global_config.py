from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from pathlib import Path

basedir = Path(__file__).resolve().parent
DATABASE = "flaskr.db"

SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(basedir).joinpath(DATABASE)}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
USERNAME = "admin"
PASSWORD = "admin"
SECRET_KEY = "change_me"

# create and initialize a new Flask app
app = Flask(__name__)
# load the config
app.config.from_object(__name__)
# init sqlalchemy
db = SQLAlchemy(app)
