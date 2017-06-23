
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(config["default"])
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = "basic"
login_manager.login_view = "login"
migrate = Migrate(app, db)

from . import views, models
