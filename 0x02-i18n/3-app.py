#!/usr/bin/env python3
"""
Flask app
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config(object):

    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    """ Configuration Class for Babel 
        to parametrize your templates.
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'



app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)



@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """Renders a Basic Template for Babel Implementation
        Use the message IDs home_title and home_header.
    """
    return render_template("3-index.html")



@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
