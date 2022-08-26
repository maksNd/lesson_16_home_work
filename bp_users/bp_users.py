import json
from db.model import db, User
from flask import Blueprint, request

bp_users = Blueprint('bp_users', __name__)


@bp_users.route('/')
def pg_all_users():
    all_users = User.query.all()
    users_response = []

    for user in all_users:
        users_response.append({'id': user.id,
                               'first_name': user.first_name,
                               'last_name': user.last_name,
                               'age': user.age,
                               'email': user.email,
                               'role': user.role,
                               'phone': user.phone})
    return json.dumps(users_response, indent=2)


@bp_users.route('/<int:id>')
def pg_user_by_id(id):
    user_by_id = User.query.get(id)
    if user_by_id is None:
        return 'user not found'

    user = {'id': user_by_id.id,
            'first_name': user_by_id.first_name,
            'last_name': user_by_id.last_name,
            'age': user_by_id.age,
            'email': user_by_id.email,
            'role': user_by_id.role,
            'phone': user_by_id.phone}
    return json.dumps(user)


@bp_users.route('/', methods=['POST'])
def add_new_user():
    data_for_new_user = request.json
    new_user = User(
        first_name=data_for_new_user.get('first_name'),
        last_name=data_for_new_user.get('last_name'),
        age=data_for_new_user.get('age'),
        email=data_for_new_user.get('email'),
        role=data_for_new_user.get('role'),
        phone=data_for_new_user.get('phone')
    )
    db.session.add(new_user)
    db.session.commit()
    return 'user added'


@bp_users.route('/<int:pk>', methods=['PUT'])
def update_user(pk):
    data_for_update_user = request.json
    user_for_update = User.query.get(pk)

    user_for_update.first_name = data_for_update_user.get('first_name')
    user_for_update.last_name = data_for_update_user.get('last_name')
    user_for_update.age = data_for_update_user.get('age')
    user_for_update.email = data_for_update_user.get('email')
    user_for_update.role = data_for_update_user.get('role')
    user_for_update.phone = data_for_update_user.get('phone')
    db.session.add(user_for_update)
    db.session.commit()
    return 'user updated'


@bp_users.route('/<int:pk>', methods=['DELETE'])
def delete_user(pk):
    user_for_delete = User.query.get(pk)
    db.session.delete(user_for_delete)
    db.session.commit()
    return 'user deleted'
