from flask import Flask
from app.views.redflag import bp
from app.views.user import bp2
from flask_jwt_extended import (
    JWTManager
)


def initialise_app():
    """Function that creates flask instance app"""
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.register_blueprint(bp2)
    app.config['JWT_SECRET_KEY'] = 'qwerty'
    jwt = JWTManager(app)
    return app
