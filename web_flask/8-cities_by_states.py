#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with states and cities"""
    states = storage.all(State)
    cities = storage.all(City)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    sorted_cities = sorted(cities.values(), key=lambda city: city.name)
    return render_template('8-cities_by_states.html',
                           states=sorted_states, cities=sorted_cities)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
