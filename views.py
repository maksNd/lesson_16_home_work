import json

from flask import Flask
from db.db import app, User, Order, Offer


@app.route('/users')
def page_users():
    all_users = User.query.all()
    users_response = []

    for user in all_users:
        users_response.append({'id': user.pk,
                               'first_name': user.first_name,
                               'last_name': user.last_name,
                               'age': user.age,
                               'email': user.email,
                               'role': user.role,
                               'phone': user.phone})
    return json.dumps(users_response, indent=2)


@app.route('/users/<int:pk>')
def page_user_by_pk(pk):
    user_by_pk = User.query.get(pk)
    if user_by_pk is None:
        return 'user not found'

    user = {'id': user_by_pk.pk,
            'first_name': user_by_pk.first_name,
            'last_name': user_by_pk.last_name,
            'age': user_by_pk.age,
            'email': user_by_pk.email,
            'role': user_by_pk.role,
            'phone': user_by_pk.phone}
    return json.dumps(user)


@app.route('/orders')
def page_orders():
    all_orders = Order.query.all()
    orders_response = []

    for order in all_orders:
        orders_response.append({'id': order.pk,
                                'name': order.name,
                                'description': order.description,
                                'start_date': order.start_date,
                                'end_date': order.end_date,
                                'address': order.address,
                                'price': order.price,
                                'customer_id': order.customer_id,
                                'executor_id': order.executor_id})
    return json.dumps(orders_response, indent=2, ensure_ascii=False)


@app.route('/orders/<int:pk>')
def page_order_by_pk(pk):
    order_by_pk = Order.query.get(pk)
    if order_by_pk is None:
        return 'user not found'

    order = {'id': order_by_pk.pk,
             'name': order_by_pk.name,
             'description': order_by_pk.description,
             'start_date': order_by_pk.start_date,
             'end_date': order_by_pk.end_date,
             'address': order_by_pk.address,
             'price': order_by_pk.price,
             'customer_id': order_by_pk.customer_id,
             'executor_id': order_by_pk.executor_id}
    return json.dumps(order, indent=2, ensure_ascii=False)


app.run()
