from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class RegistrationForm(FlaskForm):
    fullname = StringField('fullname', [
        validators.Length(min=4, max=50), validators.DataRequired()])
    username = StringField('username', [validators.Length(min=4, max=50)])
    email = StringField('email', [validators.Length(min=4, max=50), validators.Email()]) 
    password = PasswordField('password', [
        validators.Length(min=4, max=50), validators.DataRequired(),
        validators.EqualTo('confirm_password', message="password must match")])
    phone = StringField('phone', [validators.Length(min=4, max=50)])
    confirm_password = PasswordField('confirm_password', [
        validators.Length(min=4, max=50)])


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        validators.DataRequired("Please enter your email."),
        validators.Email("This field requires a valid email address.")
    ])
    # username = StringField('Username', validators=[validators.Length(min=4, max=50)])
    password = PasswordField('Password', validators=[
        validators.DataRequired("Please enter a password.")
    ])
