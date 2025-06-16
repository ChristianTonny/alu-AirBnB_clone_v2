#!/usr/bin/python3
"""
A Flask web application with routes including HTML template rendering
Route: / displays "Hello HBNB!"
Route: /hbnb displays "HBNB"
Route: /c/<text> displays "C " followed by the value of text variable
Route: /python/<text> displays "Python " followed by the value of text variable
Route: /number/<n> displays "n is a number" only if n is an integer
Route: /number_template/<n> displays HTML page only if n is an integer
"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return n is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return HTML template with number only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
