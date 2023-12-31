#!/usr/bin/env python3
"""
Define a get_timezone function and use the
babel.timezoneselector decorator
"""
from flask import Flask, render_template, request, g
from typing import Any, Union
from flask_babel import Babel, format_datetime
import pytz
from pytz import exceptions
from datetime import datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class that has a LANGUAGES class attribute
    equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object("app.Config")


@app.route("/", strict_slashes=False)
def hello_world() -> Any:
    """
    return index.html template that simply outputs
    “Welcome to Holberton” as page title (<title>) and
    “Hello world” as header (<h1>)
    """
    return render_template("index.html")


@babel.localeselector
def get_locale() -> Any:
    """
    determine the best match with our supported languages
    """
    if "locale" in request.args:
        if request.args["locale"] in app.config["LANGUAGES"]:
            return request.args["locale"]

    elif g.user and g.user.get("locale") and g.user.get("locale")\
            in app.config["LANGUAGES"]:
        return g.user.get("locale")

    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[dict, None]:
    """
    Define a get_user function that returns a user dictionary
    or None if the ID cannot be found or if login_as was not passed
    """
    if "login_as" in request.args:
        result = int(request.args["login_as"])
        dic = users.get(result)

        if dic:
            return dic

    return None


@app.before_request
def before_request() -> None:
    """
    Define a before_request function and use the app.before_request
    decorator to make it be executed before all other functions.
    before_request should use get_user to find a user if any, and
    set it as a global on flask.g.user
    """
    g.user = get_user()
    g.current_time = format_datetime(datetime.now())


@babel.timezoneselector
def get_timezone() -> Any:
    """
    Define a get_timezone function and use
    the babel.timezoneselector decorator
    """
    timezone_user = request.args.get("timezone", None)
    if timezone_user:
        try:
            return pytz.timezone(timezone_user).zone

        except exceptions.UnknownTimeZoneError:
            return "UTC"

    if g.user:
        try:
            return pytz.timezone(g.user.get("timezone")).zone

        except exceptions.UnknownTimeZoneError:
            return "UTC"

    default_timezone = app.config['BABEL_DEFAULT_TIMEZONE']
    return request.accept_languages.best_match([default_timezone])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)