from flask import Flask, abort, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask import session
from flask import redirect, url_for
import os
from src.models import db, User
from src.Blueprints.post import Post



app=Flask(__name__)
app.secret_key = os.urandom(24)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login', methods=['GET', 'POST'])
def handle_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id

            session['user']= {
        
                'email' : user.email,
                'username':user.name,
                'user_id':user.id,
                'pfp':user.pfp
                              }
                        
            return redirect('/')

        return 'Invalid email or password'
    
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
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        new_user = User( name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        session['user_id']=new_user.id
        return redirect('/')
    return redirect('/')

    return render_template('register.html')







if __name__ == "__main__":
    app.run(debug=True)