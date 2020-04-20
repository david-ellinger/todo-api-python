from app.config.base import Config as BaseConfig


class Config(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://sa:password@db:5432/todo_db"
