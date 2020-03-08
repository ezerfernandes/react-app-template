import time
from flask import Flask


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", None)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}