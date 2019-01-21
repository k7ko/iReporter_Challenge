from flask import Flask
from app.routes.main1 import bp
from app.routes.main2 import bp2

def initialise_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.register_blueprint(bp2)

    return app