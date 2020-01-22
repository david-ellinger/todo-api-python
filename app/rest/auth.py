# from app.app import db,auth
from flask import request, jsonify, current_app
from app.models.User import User
from app.models.Task import Task
import logging
import json
from flask import Blueprint, jsonify, current_app

"""
This file is used to provide some helper functions during development. It is expected to remove this later on.
"""
authentication_blueprint = Blueprint("authentication", __name__, url_prefix="/v0.1/auth")



@auth.get_password
def get_pw(username):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return user.password
    else:
        return None


@authentication_blueprint.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    user = User(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'response': 'User ' + username + ' created successfully'
    })

@authentication_blueprint.route('/add_task', methods=['POST'])
@auth.login_required
def add_task():
    content = request.form['content']
    task = Task(content=content, user=User.query.filter_by(username=auth.username()).first())
    db.session.add(task)
    db.session.commit()
    return jsonify({
        'username': auth.username(),
        'task-id': task.id,
        'content': task.content
    })


@authentication_blueprint.route('/remove_task', methods=['POST'])
@auth.login_required
def remove_task():
    task_id = request.form['task_id']
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({
            'status': 'Failed'
        })
    deleted_task = jsonify({
        'status': 'success',
        'task_id': task.id,
        'content': task.content,
        'task_completed': task.done
    })
    db.session.delete(task)
    db.session.commit()
    return deleted_task


@authentication_blueprint.route('/mark_task_as_done', methods=['POST'])
@auth.login_required
def mark_task_as_done():
    task_id = request.form['task_id']
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({
            'status': 'Failed'
        })
    task.done = True
    task.end_date = datetime.datetime.now()
    db.session.commit()
    return jsonify({
        'content': task.content,
        'add_date': task.add_date,
        'end_date': task.end_date,
        'task_completed': task.done
    })


@authentication_blueprint.route('/show_tasks', methods=['GET'])
@auth.login_required
def list_all_tasks():
    user = User.query.filter_by(username=auth.username()).first()
    if user is None:
        return jsonify({
            'status': 'failed'
        })
    task_list = {}
    for task in user.tasks:
        task_list[task.id] = {'content': task.content,
                              'add_date': task.add_date,
                              'task_completed': task.done}
