from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
@app.route('/')
def index():
    return"test"

if __name__ == "__main__":
    app.run(debug=True)