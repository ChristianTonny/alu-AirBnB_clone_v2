#!/usr/bin/python3
"""
A Flask web application with routes for /, /hbnb, /c/<text>, and /python/<text>
Route: / displays "Hello HBNB!"
Route: /hbnb displays "HBNB"  
Route: /c/<text> displays "C " followed by the value of text variable
Route: /python/<text> displays "Python " followed by the value of text variable
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return C followed by text with underscores replaced by spaces"""
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Return Python followed by text with underscores replaced by spaces"""
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
