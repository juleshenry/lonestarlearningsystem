# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    first_name = StringField(
        "First Name",
        validators=[
            DataRequired(),
            Length(min=2, max=16, message="Name must have two to twenty characters"),
        ],
    )
    last_name = StringField(
        "First Name",
        validators=[
            DataRequired(),
            Length(min=2, max=16, message="Name must have two to twenty characters"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, max=20, message="Password must contain 8 characters"),
            EqualTo("password_confirm", message="Passwords must match"),
        ],
    )
    password_confirm = StringField(
        label="Password confirm", validators=[Length(min=8, max=20)]
    )
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])


class ScheduleForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("First Name", validators=[DataRequired()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, max=20, message="Password must contain 8 characters"),
            EqualTo("password_confirm", message="Passwords must match"),
        ],
    )
    password_confirm = StringField(
        label="Password confirm", validators=[Length(min=6, max=10)]
    )
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
