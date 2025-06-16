#!/usr/bin/python3
"""
Flask web application for HBNB filters
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
    """Display a HTML page with states and amenities filters"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
    
    return render_template('10-hbnb_filters.html', 
                         states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)