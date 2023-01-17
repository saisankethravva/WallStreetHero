from flask import Flask
import os

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from stockapi import vault

db = SQLAlchemy()

app = Flask(__name__)

# Routes
from stockapi.routes import stock_api_blueprint

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
with app.app_context():
    app.register_blueprint(stock_api_blueprint)

# DB
user = vault.username
passw = vault.password
dbname = vault.database
dbhost = vault.dbhost
app.config[
    'SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://' + user + ':' + passw + '@' + dbhost + '/' + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

