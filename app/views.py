from flask import render_template, flash, redirect, url_for
from app import app
from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import login_required, login_user


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("index"))
        flash("Invalid usrname or passwd")
    return render_template("login.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def method_name():
    form = RegisterForm()
    return render_template("register.html", form=form)


@app.route("/secret")
@login_required
def secret():
    return "Only authenticated users are allowed"
