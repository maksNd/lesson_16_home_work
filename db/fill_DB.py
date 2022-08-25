import json
from model import db, User, Offer, Order

db.drop_all()
db.create_all()

with open('db/json_files/users.json') as file:
    users_from_json = json.load(file)

users = [User(**row) for row in users_from_json]

with open('db/json_files/orders.json', encoding='utf-8') as file:
    orders_from_json = json.load(file)

orders = [Order(**row) for row in orders_from_json]

with open('db/json_files/offers.json') as file:
    offers_from_json = json.load(file)

offers = [Offer(**row) for row in offers_from_json]

db.session.add_all(users)
db.session.add_all(orders)
db.session.add_all(offers)
db.session.commit()

# print(User.query.first().first_name)
