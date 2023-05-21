#!/usr/bin/python3
"""A Flask web application server.

This script starts a Flask web application that listens on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Display the string 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display the string 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """
    Display the letter 'C' followed by the value of the text variable.
    Replace underscore (_) symbols with spaces in the text variable.
    """
    return "C {}".format(text.replace("_", " "))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display 'Python ' followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
