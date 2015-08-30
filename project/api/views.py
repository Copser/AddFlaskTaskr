# project/api/views.py
from functools import wraps
from flask import flash, redirect, jsonify, \
    session, url_for, Blueprint

from project import db
from project.models import Task

# Config
api_blueprint = Blueprint('api', __name__)


# Helper Functions
def login_required(test):
    """TODO: Docstring for login_required.
    :returns: TODO

    """
    @wraps(test)
    def wrap(*args, **kwargs):
        """TODO: Docstring for wrap.
        :returns: TODO

        """
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


def open_tasks():
    """TODO: Docstring for open_tasks.
    :returns: TODO

    """
    return db.session.query(Task).filter_by(
        status='1').order_by(Task.due_date.asc())


def closed_tasks(arg1):
    """TODO: Docstring for closed_tasks.

    :arg1: TODO
    :returns: TODO

    """
    return db.session.query(Task).filter_by(
        status='0').order_by(Task.due_date.asc())


# Routes
@api_blueprint.route('/api/v1/tasks/')
def api_tasks():
    results = db.session.query(Task).limit(10).offset(0).all()
    json_results = []
    for result in results:
        data = {
            'task_id': result.task_id,
            'task_name': result.name,
            'due_date': str(result.due_date),
            'priority': result.priority,
            'posted date': str(result.posted_date),
            'status': result.status,
            'user_id': result.user_id
            }
        json_results.append(data)
    return jsonify(items=json_results)


@api_blueprint.route('/api/v1/tasks/<int:task_id>')
def task(task_id):
    """TODO: Docstring for task.
    :returns: TODO

    """
    result = db.session.query(Task).filter_by(task_id=task_id).first()
    if result:
        json_result = {
            'task_id': result.task_id,
            'task_name': result.name,
            'task.due_date': str(result.due_date),
            'priority': result.priority,
            'posted_date': str(result.posted_date),
            'status': result.status,
            'user_id': result.user_id
        }
        return jsonify(items=json_result)
    else:
        result = {"error": "Element does not exist"}
        return jsonify(result)
