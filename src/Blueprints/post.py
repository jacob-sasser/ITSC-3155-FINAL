from flask import Blueprint, abort, redirect, render_template, request, session, url_for
import sqlalchemy
from datetime import datetime, timedelta
from models import Post, User, db, Reply



router=Blueprint('posts_router', __name__, url_prefix='/posts')
@router.get('/<post_id>')
def create_post(post_id):
    title= request.form.get('title', '')
    user_id=session['user_id'].get('user_id')
    
    time=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    body=request.form.get('body','')
    byBusiness = session['user_id'].get('user_id')
    if title == '' or body=='':
        abort()
    else: 
        newPost= Post(user_id=user_id, title=title, body=body, timestamp=time,byBusiness=byBusiness )
        db.session.add(newPost)
        db.session.commit()


@router.get('/<int:post_id>/') 
def create_reply(post_id):
    
    user_id=session['user_id'].get('user_id')
    
    time=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    body=request.form.get('body','')
    

    if body=='':
        abort()
    else: 
        newReply= Reply(user_id=user_id, post_id= post_id, body=body, timestamp=time)
        db.session.add(newReply)
        db.session.commit()

