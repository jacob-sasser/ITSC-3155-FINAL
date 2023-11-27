from flask import Blueprint, abort, redirect, render_template, request, session, url_for


import sqlalchemy
from datetime import datetime, timedelta
from models import Post, User, db


router=Blueprint('posts_router', __name__, url_prefix='/posts')
@router.get('/<post_id>')
def create_post(post_id):
    title= request.form.get('title', '')
    user_id=session['user'].get('user_id')
    
    time=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    body=request.form.get('body','')
    if title == '' or body=='':
        abort()
    else: 
        newPost= Post(user_id=user_id, title=title, body=body, timestamp=time)
        db.session.add(newPost)
        db.session.commit()
        
    