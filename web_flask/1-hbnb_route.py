#!/usr/bin/python3
"""
A Flask web application with routes for / and /hbnb
Route: / displays "Hello HBNB!"
Route: /hbnb displays "HBNB"
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return Hello HBNB! message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB message"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
