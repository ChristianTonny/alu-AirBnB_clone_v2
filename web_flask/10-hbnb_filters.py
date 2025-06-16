#!/usr/bin/python3
"""
A Flask web application that displays HBNB filters
Route: /hbnb_filters displays HTML page with filters for states, cities, and amenities
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display HTML page with HBNB filters"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
