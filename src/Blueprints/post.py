from flask import Blueprint, abort, redirect, render_template, request, session, url_for
import sqlalchemy
from datetime import datetime, timedelta
from src.models import Post, db, Reply
from flask import session, redirect, url_for
import os




# router=Blueprint('posts_router', __name__, url_prefix='/posts')
# @router.get('/<post_id>')
# def create_post(post_id):
#     title= request.form.get('title', '')
#     user_id=session['user_id'].get('user_id')
    
#     time=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     body=request.form.get('body','')
#     byBusiness = session['user_id'].get('user_id')
#     if title == '' or body=='':
#         abort()
#     else: 
#         newPost= Post(user_id=user_id, title=title, body=body, timestamp=time,byBusiness=byBusiness )
#         db.session.add(newPost)
#         db.session.commit()


# @router.get('/<int:post_id>/') 
# def create_reply(post_id):
    
#     user_id=session['user_id'].get('user_id')
    
#     time=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#     body=request.form.get('body','')
    

#     if body=='':
#         abort()
#     else: 
#         newReply= Reply(user_id=user_id, post_id= post_id, body=body, timestamp=time)
#         db.session.add(newReply)
#         db.session.commit()

router = Blueprint('posts_router', __name__, url_prefix='/posts')

@router.route('/create', methods=['POST'])
def create_post():
    title = request.form.get('title', '')
    body = request.form.get('body', '')
    if not title or not body:
        abort(400)  # Bad Request

    user_id = session.get('user_id')
    byBusiness = session.get('is_business', False) 
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    newPost = Post(user_id=user_id, title=title, body=body, timestamp=time, byBusiness=byBusiness)
    db.session.add(newPost)
    db.session.commit()

    return redirect(url_for('index')) 

@router.route('/<int:post_id>/reply', methods=['POST'])
def create_reply(post_id):
    body = request.form.get('body', '')
    if not body:
        abort(400) 
    user_id = session.get('user_id')
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    newReply = Reply(user_id=user_id, post_id=post_id, body=body, timestamp=time)
    db.session.add(newReply)
    db.session.commit()

    return redirect(url_for('index'))

@router.route('/<int:post_id>', methods=['GET'])
def view_post(post_id):
    user_id=session.get('user_id')
    post = Post.query.get_or_404(post_id)
    replies = Reply.query.filter_by(post_id=post_id).all()
    return render_template('individualpost.html', post=post, replies=replies)
