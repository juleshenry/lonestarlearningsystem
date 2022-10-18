# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):

    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    # phone_number = db.Column(db.)
    password = db.Column(db.String(500))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def __repr__(self):
        return str(self.id) + " - " + str(self.first_name) +" - " + str(self.last_name)

    def save(self):

        # inject self into db session
        db.session.add(self)

        # commit change and save the object
        db.session.commit()

        return self
