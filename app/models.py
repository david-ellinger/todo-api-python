# from flask.ext.sqlalchemy import sqlalchemy

import datetime
import uuid

from sqlalchemy.dialects.postgresql import UUID

from app.database import db

# from flask_sqlalchemy import SQLAlchemy


class Todo(db.Model):
    __tablename__ = "todo"
    id = db.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    category_id = db.Column(
        "category_id", UUID(as_uuid=True), db.ForeignKey("category.id"), nullable=False
    )
    priority_id = db.Column(
        "priority_id", UUID(as_uuid=True), db.ForeignKey("priority.id"), nullable=False
    )
    description = db.Column("description", db.Unicode)
    creation_date = db.Column(
        "created_data", db.DateTime, default=datetime.datetime.utcnow
    )
    is_done = db.Column("is_done", db.Boolean, default=False)

    priority = db.relationship("Priority", foreign_keys=priority_id)
    category = db.relationship("Category", foreign_keys=category_id)


class Priority(db.Model):
    __tablename__ = "priority"
    id = db.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = db.Column("name", db.Unicode)


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    name = db.Column("name", db.Unicode)
