from flask import current_app
from db.fill_DB import fill_db
from bp_users.bp_users import bp_users
from bp_orders.bp_orders import bp_orders
from bp_offers.bp_offers import bp_offers

app = current_app

fill_db()

app.register_blueprint(bp_users, url_prefix='/users/')
app.register_blueprint(bp_orders, url_prefix='/orders/')
app.register_blueprint(bp_offers, url_prefix='/offers/')

if __name__ == '__main__':
    app.run()
