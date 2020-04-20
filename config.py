import os


class Config(object):
    ENV = os.environ["ENV"]
    CSRF_ENABLED = True
    SECRET_KEY = "SOME_RANDOM_SECRET_KEY"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql+psycopg2://sa:password@db:5432/todo_db",
    )


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql+psycopg2://sa:password@db:5432/todo_db",
    )
