from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from datetime import datetime
db= SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))
    pfp=db.Column(db.String)
    def __repr__(self):
        return '<User %r>' % self.username
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('User.user_id'))
    title = db.Column(db.String(80))
    body = db.Column(db.String())
    timestamp =db.Column(db.String)
