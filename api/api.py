import time
import os
from flask import Flask
import connexion


def create_app():
    #app = Flask(__name__)
    app = connexion.App(__name__, specification_dir='./')
    app.add_api('swagger.yml')
    app.config.from_envvar("APPLICATION_SETTINGS")
    app.config['MAIL_ENABLED'] = os.environ.get("MAIL_ENABLED", default="false").lower() \
        in ("1", "t", "true")
    return app


app = create_app()


@app.route('/time')
def get_current_time():
    return {'time': time.time()}