import json
from db.model import db, User, Offer, Order


def get_data_from_json(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def fill_DB():
    db.drop_all()
    db.create_all()

    users_from_json = get_data_from_json('db/json_files/users.json')
    orders_from_json = get_data_from_json('db/json_files/orders.json')
    offers_from_json = get_data_from_json('db/json_files/offers.json')

    users = [User(**row) for row in users_from_json]
    orders = [Order(**row) for row in orders_from_json]
    offers = [Offer(**row) for row in offers_from_json]

    db.session.add_all(users)
    db.session.add_all(orders)
    db.session.add_all(offers)
    db.session.commit()
