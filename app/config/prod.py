from app.config.base import Config as BaseConfig


class Config(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://sa:password@postgres:5432/todo_db"
