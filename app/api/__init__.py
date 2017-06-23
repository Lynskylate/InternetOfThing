from flask import Blueprint

api = Blueprint("flask", __name__)

from . import views
