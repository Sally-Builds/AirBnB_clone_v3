#!/usr/bin/python3

from flask import Flask
from models import storage
# from api.v1.views import app_views
from api.v1.views import app_views

app = Flask("__name__")


@app.teardown_appcontext
def close_db(obj):
    """ calls methods close() """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
