from app.models import Todo, Category, Priority
from app.database import db
from flask import current_app


def populate(count):

    with current_app.app_context():
        db.drop_all()
        db.create_all()
        priority_one = Priority()
        priority_one.id = 1
        priority_one.name = "HIGH"
        priority_one.value = 1

        priority_two = Priority()
        priority_two.id = 1
        priority_two.name = "HIGH"
        priority_two.value = 1

        priority_three = Priority()
        priority_one.id = 1
        priority_one.name = "HIGH"
        priority_one.value = 1

        db.session.add_all([priority_one, priority_two, priority_three])

	# for i in range(row_count):

