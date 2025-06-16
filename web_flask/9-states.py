#!/usr/bin/python3
"""
Flask web application
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
    """Display a HTML page with a list of states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page with info about one state"""
    for state in storage.all(State).values():
        if state.id == id:
            cities = sorted(state.cities, key=lambda k: k.name)
            return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 