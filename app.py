from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from src.models import User, Post, Reply
from src.models import db
from src.Blueprints.post import router as post_router
from src.Blueprints.userpage import router as user_router

from flask import flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
app.register_blueprint(user_router)
app.register_blueprint(post_router)

@app.route('/index')
def index():
    
   
    #just test for logout function
    if 'user_id' in session:
        flash('user_id')
        
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






@app.get('/logout')
def logout():
    if 'user_id' not in session:
        return redirect('/login')
    del session['user_id']
    return redirect('/index')

if __name__ == "__main__":
    app.run(debug=True)
