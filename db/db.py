import json
from sqlalchemy import create_engine, Column, Text, Integer, String, ForeignKey
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base, sessionmaker, Query

# engine = create_engine("sqlite:///users_orders.db")
# db = declarative_base(bind=engine)
# Session = sessionmaker(bind=engine)


app = Flask(__name__)
app.json.ensure_ascii = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users_orders.db"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    pk = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(Text(100))
    age = Column(Integer)
    email = Column(Text(100))
    role = Column(Text(100))
    phone = Column(Text(20))


class Order(db.Model):
    __tablename__ = 'orders'
    pk = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(100))
    start_date = Column(String(100))
    end_date = Column(String(100))
    address = Column(String(100))
    price = Column(Integer)
    customer_id = Column(Integer, ForeignKey(User.pk), nullable=False)
    executor_id = Column(Integer, ForeignKey(User.pk), nullable=False)


class Offer(db.Model):
    __tablename__ = 'offers'
    pk = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(Order.pk), nullable=False)
    executor_id = Column(Integer, ForeignKey(User.pk), nullable=False)


db.drop_all()
db.create_all()

with open('db/json_files/users.json') as file:
    users_from_json = json.load(file)

users = []

for user in users_from_json:
    users.append(User(
        pk=user['id'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        age=user['age'],
        email=user['email'],
        role=user['role'],
        phone=user['phone']
    ))

with open('db/json_files/orders.json', encoding='utf-8') as file:
    orders_from_json = json.load(file)

orders = []

for order in orders_from_json:
    orders.append(Order(
        pk=order['id'],
        name=order['name'],
        description=order['description'],
        start_date=order['start_date'],
        end_date=order['end_date'],
        address=order['address'],
        price=order['price'],
        customer_id=order['customer_id'],
        executor_id=order['executor_id']
    ))

with open('db/json_files/offers.json') as file:
    offers_from_json = json.load(file)

offers = []

for offer in offers_from_json:
    offers.append(Offer(
        pk=offer['id'],
        order_id=offer['order_id'],
        executor_id=offer['executor_id']
    ))

# with Session() as session:
db.session.add_all(users)
db.session.add_all(orders)
db.session.add_all(offers)
db.session.commit()


print(User.query.first().first_name)