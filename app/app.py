import os

from flask import Flask

# from flask_graphql import GraphQLView
from app.database import db
from app.mock_data import populate

# from flask_sqlalchemy import SQLAlchemy


def create_app():

    app = Flask(__name__)
    load_config(app)
    app.app_context().push()
    try:
        db.init_app(app)
        populate(2)
    except Exception as e:
        print("Failed to initialize database")
        print(e)

    # from app.schema import schema

    # app.add_url_rule(
    #     "/graphql",
    #     view_func=GraphQLView.as_view("graphql",
    # schema=schema, graphiql=True),
    # )

    # @app.before_first_request
    # def initialize_database():
    #     """ Create all tables """
    #     print("Creating all tables")
    #     db.create_all()

    # @app.route("/")
    # def hello_world():
    #     return "Hello World!"

    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     db.session.remove()

    return app


def load_config(app):
    config_name = os.environ["ENV"]
    print(f"Loading {config_name} config")
    app.config.from_object(f"app.config.{config_name}.Config")


# This is required for flask to bootstrap without gunicorn for development
if os.environ.get("FLASK_DEBUG"):
    app = create_app()
