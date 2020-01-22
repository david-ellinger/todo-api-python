# from app.app import db,auth
from flask import Blueprint

"""
This file is used to provide some helper functions during development. It is expected to remove this later on.
"""
home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.route('/', methods=['GET'])
def ping():
    return "Hello World"
