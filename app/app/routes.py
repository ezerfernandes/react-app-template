from flask import request, render_template, make_response, url_for, jsonify, abort
from flask import current_app as app
from flask_login import LoginManager
from datetime import datetime as dt
from .models import db, User
import time


login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    return User,query.get(user_id)


@app.route('/user/create', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if username is None or email is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400) # existing user
    if User.query.filter_by(email=email).first() is not None:
        abort(400) # existing user
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201
    #return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}


@app.route('/hello', methods=['GET'])
def test():
    return "Hello world!"


@app.route('/time')
def get_current_time():
    return {'time': time.time()}