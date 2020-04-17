import os


class Config(object):
    ENV = os.environ['ENV']
    CSRF_ENABLED = True
    SECRET_KEY = "SOME_RANDOM_SECRET_KEY"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql+psycopg2://username:password@0.0.0.0:5401/database_name')

  
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql+psycopg2://username:password@0.0.0.0:5401/database_name')
