from flask import Flask, render_template, request, session, redirect, url_for, json, Blueprint,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from src.models import User, Post, Reply,db
from src.Blueprints.post import router
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(router)



def get_info():
    user_name = None
    user_email=None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user_name = user.name
            user_email = user.email
            return user_name, user.email


@app.route('/index')
def index():
    user_name = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user:
            user_name = user.name
    return render_template("index.html", user_name=user_name)

#just so I dont have to type /index it annoys me
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def handle_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(name=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.user_id

            flash('Login successful! Welcome back, {}'.format(username), 'success')
            return redirect(url_for('index'))

        flash('Login failed. Invalid username or password', 'error')

    return render_template('login.html')


@app.route('/edit_account', methods=['GET', 'POST'])

def edit_account():
    current_username = get_info()[0]
    current_email=get_info()[1]

    if request.method=='POST':
        
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        
        new_username= request.form.get('new_username')
        
        new_password = request.form.get('new_password')
        new_email = request.form.get('new_email')
        hashed_password = generate_password_hash(new_password)

        
        

        if user:
            if new_username:
                user.name= new_username
                
            if new_password:
                
                user.password=hashed_password
                
                
            if new_email:
                user.email=new_email
        db.session.commit()
        return redirect('/index')
        
    return render_template("edit_account.html",current_username=current_username, current_email=current_email )



@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def handle_registration():
    if request.method == 'POST':
        name = request.form.get('username', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')

        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.user_id

        flash('Registration successful! Welcome, {}'.format(name), 'success')

        return redirect(url_for('index'))
    return redirect(url_for('register'))

@app.route('/post', methods=['GET'])
def view_posts():
    # Retrieve all posts from the database
    posts = Post.query.all()
    
    return render_template("post.html", posts=posts)
    

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title', '')
        body = request.form.get('body', '')
        user_id = session.get('user_id')
        post_id=session.get('post_id')
        if title and body:
            new_post = Post(user_id=user_id,  title=title, body=body)
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully', 'success')
            return redirect(url_for('index'))

        flash('Title and body are required to create a post.', 'error')
    return render_template("post.html")
        
@app.route('/<int:post_id>/create_reply', methods=['POST'])
def reply_to_post(post_id):
    if request.method == 'POST':
        user_id = session.get('user_id')
        body = request.form.get('body', '')

        if body:
            new_reply = Reply(user_id=user_id, post_id=post_id, body=body)
            db.session.add(new_reply)
            db.session.commit()
            flash('Reply added successfully', 'success')
            return redirect(url_for('post'))

        flash('Reply cannot be empty.', 'error')
    return render_template("post.html", post_id=post_id)
@app.get('/logout')
def logout():
    if 'user_id' not in session:
        return redirect('/login')
    del session['user_id']
    return redirect('/index')


if __name__ == "__main__":
    app.run(debug=True)
