from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from datetime import datetime

db= SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))
    pfp=db.Column(db.String)
    business=db.Column(db.Boolean(), default=False, nullable=False)

    def getUser(self):
        return User.query.get(self.user_id)
    def isBusiness(self):
        return User.query.get(self.business)
    
    def __repr__(self):
        return '<User %r>' % self.username
    

class Post(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(80))
    body = db.Column(db.String())
    timestamp =db.Column(db.String())
    byBusiness = db.Column(db.Boolean, db.ForeginKey('User.business'))
    
    
    def getUser(self):
        return Post.query.get(self.user_id)
    
    def getPost(self):
        return Post.query.get(self.post_id)
    
    def getTimestamp(self):
        return Post.query.get(self.timestamp)
    

    def isBusiness(self):
        return Post.query.get(self.byBusiness)

    
class Reply(db.Model):
    __tablename__ = 'replies'
    user_id=db.Column(db.Integer, db.ForeignKey('User.user_id'))
    post_id=db.Column(db.Integer, db.ForeignKey('posts.post_id'))
    reply_id=db.Column(db.Integer, nullable=False, primary_key=True)
    body= db.Column(db.String, nullable = False)
    timestamp =db.Column(db.String())

