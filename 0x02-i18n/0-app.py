#!/usr/bin/env python3
"""Basic Flask app in 0-app.py
"""

from flask import Flask, render_template
from flask_babel import Babel
from typing import Any

app = Flask(__name__)
babel = Babel(app)

app.config['LANGUAGES'] = {
    'en': 'English',
}

#set language to english
@babel.localeselector
def get_locale():
    return 'en'

#create route
@app.route('/', strict_slashes=False)
def hello_world() -> Any:
    """Return index.html and output a 
    message
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)