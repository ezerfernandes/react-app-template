from flask import request, render_template, make_response, url_for, jsonify, abort, g
from flask import current_app as app
from flask_login import LoginManager
from flask_httpauth import HTTPBasicAuth
from datetime import datetime as dt
from .models import db, User
import time


login_manager = LoginManager()
auth = HTTPBasicAuth()


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


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@app.route('/resource') #example
@auth.login_required
def get_resource():
    return jsonify({'data': f'Hello, {g.user.username}!'})


@app.route('/time') #example
def get_current_time():
    return {'time': time.time()}