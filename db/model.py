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
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(Text(100))
    age = Column(Integer)
    email = Column(Text(100))
    role = Column(Text(100))
    phone = Column(Text(20))


class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(100))
    start_date = Column(String(100))
    end_date = Column(String(100))
    address = Column(String(100))
    price = Column(Integer)
    customer_id = Column(Integer, ForeignKey(User.id), nullable=False)
    executor_id = Column(Integer, ForeignKey(User.id), nullable=False)


class Offer(db.Model):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey(Order.id), nullable=False)
    executor_id = Column(Integer, ForeignKey(User.id), nullable=False)