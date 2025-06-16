#!/usr/bin/python3
"""
A Flask web application that displays states and state details with cities
Route: /states displays HTML page with all State objects
Route: /states/<id> displays HTML page with cities of a State
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Display HTML page with list of all states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display HTML page with a specific state and its cities"""
    state = None
    for s in storage.all(State).values():
        if s.id == id:
            state = s
            break
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
