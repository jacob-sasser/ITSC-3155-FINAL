from flask import Blueprint, abort, redirect, render_template, request, session, url_for
import sqlalchemy
from datetime import datetime, timedelta
from models import Post, User, db, Reply

router=