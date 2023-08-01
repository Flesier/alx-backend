from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.config['LANGUAGES'] = {
    'en': 'English',
}

#set language to english
@babel.localselector
def get_locale():
    return 'en'

#create route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()