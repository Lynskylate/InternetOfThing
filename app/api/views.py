from . import api
from .. import db
from ..models import User
from flask import render_template, redirect


@api.route("/", methods=["GET", "POST"])
def apiindex():
    return "loveyou"
