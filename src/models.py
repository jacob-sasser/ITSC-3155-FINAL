from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey 
from datetime import datetime

db= SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = Column(db.Integer, nullable=False, primary_key=True)
    name = Column(db.String(50))
    email = Column(db.String(120), unique=True)
    password = Column(db.String(80))
    pfp=Column(db.String)
    business=Column(db.Boolean(), default=False, nullable=False)

    def getUser(self):
        return User.query.get(self.user_id)
    def isBusiness(self):
        return User.query.get(self.business)
    
    def __repr__(self):
        return '<User %r>' % self.username
    

class Post(db.Model):
    __tablename__ = 'posts'
    post_id = Column(db.Integer, primary_key=True)
    user_id=Column(db.Integer, ForeignKey('users.user_id'))
    title = Column(db.String(80))
    body = Column(db.String())
    timestamp =Column(db.String())
    byBusiness = Column(db.Boolean, ForeignKey('users.business'))
    
    
    def getUser(self):
        return Post.query.get(self.user_id)
    
    def getPost(self):
        return Post.query.get(self.post_id)
    
    def getTimestamp(self):
        return Post.query.get(self.timestamp)
    

    def isBusiness(self):
        return Post.query.get(self.byBusiness)
    def getRepliesCount(self):
        return Post.query.get(self.repliesCount)

    
class Reply(db.Model):
    __tablename__ = 'replies'
    user_id=Column(db.Integer, ForeignKey('User.user_id'))
    post_id=Column(db.Integer, ForeignKey('posts.post_id'))
    reply_id=Column(db.Integer, nullable=False, primary_key=True)
    body= Column(db.String, nullable = False)
    timestamp =Column(db.String())

