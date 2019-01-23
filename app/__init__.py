from flask import Flask
from app.views.redflag import bp
from app.views.user import bp2


def initialise_app():
    """Function that creates flask instance app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty'
    app.register_blueprint(bp)
    app.register_blueprint(bp2)
    return app