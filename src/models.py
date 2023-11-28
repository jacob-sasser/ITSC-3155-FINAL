from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))
    business = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.name}>'

class Post(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String(80))
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime)
    byBusiness = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Post {self.title}>'

class Reply(db.Model):
    __tablename__ = 'replies'
    reply_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))
    body = db.Column(db.String())
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Reply {self.reply_id}>'
