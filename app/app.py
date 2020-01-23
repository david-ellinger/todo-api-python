"""
This file initializes the Flask app and boostraps various modules and interfaces.
"""

from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from flasgger import Swagger
from app.rest.auth import authentication_blueprint
from app.rest.home import home_blueprint
from app.shared.shared import db
from flask_sqlalchemy import SQLAlchemy
import os
import app.config as config


DEFAULT_BLUEPRINTS = [home_blueprint, authentication_blueprint]

def create_app() -> Flask:
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_CONNECTION_URI
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.app_context().push()
  db = SQLAlchemy(app)
  db.init_app(app)
  db.create_all()

  CORS(app)

  configure_swagger(app)
  configure_blueprints(app, DEFAULT_BLUEPRINTS)
  # configure_db(app)
  return app

def configure_blueprints(
    app: Flask, blueprints
):
    """
    Registers the Flask blueprints with the flask app
    """
    # Common blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_swagger(app: Flask) -> None:
    """
    Some swagger config
    """
    app.config["SWAGGER"] = {"title": "David's Todo API", "uiversion": 3}
    Swagger(app)


def configure_db(app):
    """
    Retrieve connection string based on environment. Initialize database.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    db.init_app(app)
    with app.app_context():
        db.create_all()


# This is required for flask to bootstrap without gunicorn for development
if os.environ.get("FLASK_DEBUG"):
    app = create_app()
