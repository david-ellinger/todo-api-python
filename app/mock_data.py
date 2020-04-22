from faker import Faker
from flask import current_app

from app.database import db
from app.models import Category, Priority, Todo


def populate(count):
    fake = Faker()
    Faker.seed(0)
    with current_app.app_context():
        db.drop_all()
        db.create_all()
        low_priority = Priority(name="low")
        medium_priority = Priority(name="medium")
        high_priority = Priority(name="high")
        db.session.add_all([low_priority, medium_priority, high_priority])

        home_category = Category(name="Home")
        work_category = Category(name="Work")
        school_category = Category(name="School")
        db.session.add_all([home_category, work_category, school_category])
        Faker.seed(0)
        for _ in range(count):
            todo1 = Todo(
                category=home_category,
                priority=low_priority,
                description=fake.sentence(),
                is_done=fake.boolean(),
            )
            todo2 = Todo(
                category=work_category,
                priority=medium_priority,
                description=fake.sentence(),
                is_done=fake.boolean(),
            )
            todo3 = Todo(
                category=school_category,
                priority=high_priority,
                description=fake.sentence(),
                is_done=fake.boolean(),
            )
            db.session.add_all([todo1, todo2, todo3])

        db.session.commit()
