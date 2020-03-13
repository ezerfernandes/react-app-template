from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User
import time


@app.route('/', methods=['GET'])
def create_user():
    """Create a user."""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        new_user = User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born n raised...",
                        admin=False)
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
    return make_response(f"{new_user} successfully created!")

@app.route('/hello', methods=['GET'])
def test():
    return "Hello world!"


@app.route('/time')
def get_current_time():
    return {'time': time.time()}