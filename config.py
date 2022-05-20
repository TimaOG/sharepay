from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)
UPLOAD_FOLDER = 'static\\uploads'
app.secret_key = 'BIG DICK'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
migrate = Migrate(app, db)
maneger = LoginManager(app)

