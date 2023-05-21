#!/usr/bin/python3
"""A Flask web application.

This script starts a Flask web application that listens on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return the string 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return the string 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """
    Display the letter 'C' followed by the value of the text variable.
    Replace underscore (_) symbols with spaces in the text variable.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """
    Display the string 'Python' followed by the value of the text variable.
    If no text is provided, it defaults to 'is cool'.
    Replace underscore (_) symbols with spaces in the text variable.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """
    Display "<n> is a number" if n is an integer.

    Args:
        n (int): The number to be checked.

    Returns:
        str: The message indicating if n is a number or not.
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
