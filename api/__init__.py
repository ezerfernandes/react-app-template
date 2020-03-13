from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_envvar("APPLICATION_SETTINGS")
    app.config['MAIL_ENABLED'] = os.environ.get("MAIL_ENABLED", default="false").lower() \
        in ("1", "t", "true")
    db.init_app(app)
    with app.app_context():
        from . import routes
        db.create_all()
        return app


    

def create_app():
    app = Flask(__name__)
    app.config.from_envvar("APPLICATION_SETTINGS")
    app.config['MAIL_ENABLED'] = os.environ.get("MAIL_ENABLED", default="false").lower() \
        in ("1", "t", "true")
    return app