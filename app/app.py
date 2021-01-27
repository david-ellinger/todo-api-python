from functools import lru_cache

from typing import Optional, Iterator
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from fastapi_utils.session import FastAPISessionMaker
from pydantic import BaseSettings
import sqlalchemy as sa
from uuid import UUID

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = sa.Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = sa.Column(sa.String, nullable=False)

class DBSettings(BaseSettings):
    """ Parses variables from environment on instantiation """

    database_uri: str = "sqlite:///todo_app.db" # could break up into scheme, username, password, host, db


# def get_db() -> Iterator[Session]:
#         """ FastAPI dependency that provides a sqlalchemy session """
#         yield from _get_fastapi_sessionmaker().get_db()


# @lru_cache() # reuse session across requests
# def _get_fastapi_sessionmaker() -> FastAPISessionMaker:
#     """ This function could be replaced with a global variable if preferred """
#     database_uri = DBSettings().database_uri
#     return FastAPISessionMaker(database_uri) # check_same_thread only needed for sqlite

app = FastAPI()
engine = create_engine(
    "sqlite:///todo_app.db", connect_args={"check_same_thread": False}
)

@app.get("/")
def ping():
    return {"ping": "pong"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/{user_id}")
def get_user_name(user_id: int) -> str:
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    test_user = User(name="Darla")
    db.add(test_user)
    db.commit()
    # user = db.query(User).get(user_id)
    # username = user.name
    return "Test"


# def create_app():

#     app = Flask(__name__)
#     load_config(app)
#     app.app_context().push()
#     try:
#         db.init_app(app)
#         populate(2)
#     except Exception as e:
#         print("Failed to initialize database")
#         print(e)

#     return app


# def load_config(app):
#     config_name = os.environ["ENV"]
#     print(f"Loading {config_name} config")
#     app.config.from_object(f"app.config.{config_name}.Config")


# # This is required for flask to bootstrap without gunicorn for development
# if os.environ.get("FLASK_DEBUG"):
#     app = create_app()
