#!/usr/bin/python3
"""
A Flask web application that displays states and their cities from the database
Route: /cities_by_states displays HTML page with all State objects and their cities
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display HTML page with list of states and their cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
