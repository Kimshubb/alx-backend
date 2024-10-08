#!/usr/bin/env python3
'''Flask application
'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''theFlask Babel configuration.
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """retrieves web page locale
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def hello() -> str:
    '''the base route
    '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
