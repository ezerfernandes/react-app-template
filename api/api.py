import time
import os
from flask import Flask


app = Flask(__name__)
app.config.from_envvar("APPLICATION_SETTINGS")



@app.route('/time')
def get_current_time():
    return {'time': time.time()}