"""
Flask Application for greeting users with their name.

Author: Krzysztof Szymanek
Date: 2023-03-18

Modules:
- Flask is a micro web framework written in Python.
- render_template is a Flask function from the flask used for rendering HTML templates.
- The request object used by default in Flask a module in Flask used for handling HTTP requests.

Endpoints:
- "/" information to to suer, displays a form where users can input their name.
- "/hello"...greets the user with their name.
"""
from flask import Flask, render_template, request

main = Flask(__name__)


@main.route("/")
def hello():
    """
    Module: "hello"

    Description: When a user navigates to this route, they will see a form where they can
    enter their name. Defined in the 'hello.html' template.

    Routes:
        - '/': This route renders the 'hello.html' template.
    """
    return render_template("hello.html")


@main.route("/hello", methods=["GET", "POST"])
def greet():
    """
    Module : greet

    If the request method is POST, this function retrieves the value of the "name"
    input field from the submitted form data, and returns a greeting message with the
    provided name. Otherwise, it renders the "hello.html" template with an empty form.

    Returns:
        str or Flask response: If the request method is POST, returns a str with the
            greeting message. Differently, returns a Flask response object that renders
            the "hello.html" template with an empty form.

    Raises:
        error: if the submitted form data does not contain a "name" field.
    """
    if request.method == "POST":
        name = request.form["name"]
        greeting = "Hello " + name
        return render_template("response.html", greeting=greeting)
    return render_template("hello.html")


if __name__ == "__main__":
    main.run(debug=True)
