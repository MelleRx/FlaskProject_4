from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    mail = StringField("Электронная почта:", validators=[DataRequired()])
    password = PasswordField("Пароль:", validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    mail = StringField("Электронная почта")
    password = PasswordField("Пароль")


class OrderForm(FlaskForm):
    date = StringField("Дата")
    mail = StringField("Электронная почта")
    name = StringField("Имя")
    phone = StringField("Телефон")
    address = StringField("Адрес")
