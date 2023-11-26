from flask import Flask, abort, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask import session
from flask import redirect, url_for
import os
    


app=Flask(__name__)
app.secret_key = os.urandom(24)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
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
            return redirect(url_for('index'))

        return 'Invalid email or password'

    return render_template('login.html')


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/path-to-your-registration-handler', methods=['POST'])
def handle_registration():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return 'User registered successfully'

    return render_template('register.html')



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username



if __name__ == "__main__":
    app.run(debug=True)