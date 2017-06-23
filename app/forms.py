from flask_wtf import FlaskForm
from .models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField("邮箱", validators=[
                        Required(), Length(1, 64), Email()])
    password = PasswordField("密码", validators=[Required()])
    submit = SubmitField("登录")


class RegisteForm(FlaskForm):
    email = StringField("邮箱", validators=[
                        Required(), Length(1, 64), Email()])
    username = StringField("用户名", validators=[
        Required(), Length(4, 64)
    ])
    password = PasswordField("密码", validators=[
                             Required(), EqualTo("password2", message="两次密码输入必须一致")])
    password2 = PasswordField("确认密码", validators=[Required()])
    submit = SubmitField("注册")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("已经存在的邮箱")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("已有的用户名")
