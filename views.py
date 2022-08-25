import json

from flask import Flask
from db.model import app, User, Order, Offer


@app.route('/users/')
def page_users():
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


@app.route('/users/<int:id>')
def page_user_by_id(id):
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


@app.route('/orders/')
def page_orders():
    all_orders = Order.query.all()
    orders_response = []
    for order in all_orders:
        orders_response.append({'id': order.id,
                                'name': order.name,
                                'description': order.description,
                                'start_date': order.start_date,
                                'end_date': order.end_date,
                                'address': order.address,
                                'price': order.price,
                                'customer': User.query.get(order.customer_id).first_name,
                                'executor': User.query.get(order.executor_id).first_name})
    return json.dumps(orders_response, indent=2, ensure_ascii=False)


@app.route('/orders/<int:id>')
def page_order_by_id(id):
    order_by_id = Order.query.get(id)
    if order_by_id is None:
        return 'order not found'

    order = {'id': order_by_id.id,
             'name': order_by_id.name,
             'description': order_by_id.description,
             'start_date': order_by_id.start_date,
             'end_date': order_by_id.end_date,
             'address': order_by_id.address,
             'price': order_by_id.price,
             'customer': User.query.get(order_by_id.customer_id).first_name,
             'executor': User.query.get(order_by_id.executor_id).first_name}
    # 'customer_id': order_by_id.customer_id,
    # 'executor_id': order_by_id.executor_id}
    return json.dumps(order, indent=2, ensure_ascii=False)


app.run()
