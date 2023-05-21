#!/usr/bin/python3
"""Script that starts a Flask web application server:
Web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Method to close the session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Displays an HTML page with all states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displays an HTML page with cities of a specific state"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
