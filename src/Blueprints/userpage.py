from flask import Blueprint, abort, redirect, render_template, request, session, url_for
import sqlalchemy
from datetime import datetime, timedelta
from models import Post, User, db, Reply
from app import session
router=Blueprint('user_router',__name__)
@router.get('</name>')
def account_page(user_id):
    if 'user_id' not in session:
        abort('/index')
    else:
        return redirect("about")
    
    
    


