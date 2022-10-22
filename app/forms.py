# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField(u"Email", validators=[DataRequired()])
    password = PasswordField(u"Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    first_name = StringField(u"First Name", validators=[DataRequired()])
    last_name = StringField(u"First Name", validators=[DataRequired()])
    password = PasswordField(u"Password", validators=[DataRequired(),
        Length(min=8, max=20, message='Password must contain 8 characters'),
        EqualTo('password_confirm', message='Passwords must match')
    ])
    password_confirm = StringField(label='Password confirm', validators=[
        Length(min=6, max=10)
    ])
    email = StringField(u"Email Address", validators=[DataRequired(), Email()])
    phone_number = StringField(u"Phone Number", validators=[DataRequired()])
