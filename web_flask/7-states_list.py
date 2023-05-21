#!/usr/bin/python3
"""A flask Web App for displaying states"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Display a list of states on the states_list page"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
