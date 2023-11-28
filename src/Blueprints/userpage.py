from flask import Blueprint, abort, redirect, render_template, request, session, url_for
import sqlalchemy
from datetime import datetime, timedelta
from src.models import Post, User, db, Reply

router=Blueprint('user',__name__, url_prefix='/user')
'''@router.get('</name>')
def account_page(user_id):
    if 'user_id' not in session:
        abort('/index')
    else:
        return redirect("/about")
    return redirect("/about")
    
    '''


