import json
from db.model import db, Order, User
from flask import Blueprint, request

bp_orders = Blueprint('bp_orders', __name__)


@bp_orders.route('/')
def pg_all_orders():
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


@bp_orders.route('/<int:id>')
def pg_order_by_id(id):
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
    return json.dumps(order, indent=2, ensure_ascii=False)


@bp_orders.route('/', methods=['POST'])
def add_new_order():
    data_for_new_order = request.json
    new_order = Order(
        name=data_for_new_order.get('name'),
        description=data_for_new_order.get('description'),
        start_date=data_for_new_order.get('start_date'),
        end_date=data_for_new_order.get('end_date'),
        address=data_for_new_order.get('address'),
        price=data_for_new_order.get('price'),
        customer_id=data_for_new_order.get('customer_id'),
        executor_id=data_for_new_order.get('executor_id')
    )
    db.session.add(new_order)
    db.session.commit()
    return 'order added'


@bp_orders.route('/<int:pk>', methods=['PUT'])
def update_order(pk):
    data_for_update_order = request.json
    order_for_update = Order.query.get(pk)

    order_for_update.name = data_for_update_order.get('name')
    order_for_update.description = data_for_update_order.get('description')
    order_for_update.start_date = data_for_update_order.get('start_date')
    order_for_update.end_date = data_for_update_order.get('end_date')
    order_for_update.address = data_for_update_order.get('address')
    order_for_update.price = data_for_update_order.get('price')
    order_for_update.customer_id = data_for_update_order.get('customer_id')
    order_for_update.executor_id = data_for_update_order.get('executor_id')
    db.session.add(order_for_update)
    db.session.commit()
    return 'order updated'


@bp_orders.route('/<int:pk>', methods=['DELETE'])
def delete_order(pk):
    order_for_delete = Order.query.get(pk)
    db.session.delete(order_for_delete)
    db.session.commit()
    return 'order deleted'
