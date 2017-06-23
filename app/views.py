from flask import render_template, flash, redirect, url_for
from app import app, db
from .models import User
from .forms import LoginForm, RegisteForm
from flask_login import login_required, login_user, current_user, logout_user
from .api import api

app.register_blueprint(api, url_prefix="/api/")


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("你已经登录了")
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash("登录成功")
            return redirect(url_for("index"))
        flash("不正确的用户名或密码")
    return render_template("login.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("你已经登录了")
        return redirect(url_for("index"))
    form = RegisteForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("注册成功")
        login_user(user)
        return redirect(url_for("index"))
    return render_template("register.html", form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("注销成功")
    return redirect(url_for("index"))
