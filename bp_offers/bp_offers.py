import json
from db.model import db, Offer
from flask import Blueprint, request

bp_offers = Blueprint('bp_offers', __name__)


@bp_offers.route('/')
def pg_all_offers():
    all_offers = Offer.query.all()
    offers_response = []

    for offer in all_offers:
        offers_response.append({'id': offer.id,
                                'order_id': offer.order_id,
                                'executor_id': offer.executor_id})
    return json.dumps(offers_response, indent=2)


@bp_offers.route('/<int:id>')
def pg_offer_by_id(id):
    offer_by_id = Offer.query.get(id)
    if offer_by_id is None:
        return 'offer not found'

    offer = {'id': offer_by_id.id,
             'order_id': offer_by_id.order_id,
             'executor_id': offer_by_id.executor_id}
    return json.dumps(offer)


@bp_offers.route('/', methods=['POST'])
def add_new_offer():
    data_for_new_offer = request.json
    new_offer = Offer(
        order_id=data_for_new_offer.get('order_id'),
        executor_id=data_for_new_offer.get('executor_id')
    )
    db.session.add(new_offer)
    db.session.commit()
    return 'offer added'


@bp_offers.route('/<int:pk>', methods=['PUT'])
def update_offer(pk):
    data_for_update_offer = request.json
    offer_for_update = Offer.query.get(pk)

    offer_for_update.order_id = data_for_update_offer.get('order_id')
    offer_for_update.executor_id = data_for_update_offer.get('executor_id')
    db.session.add(offer_for_update)
    db.session.commit()
    return 'offer updated'


@bp_offers.route('/<int:pk>', methods=['DELETE'])
def delete_offer(pk):
    offer_for_delete = Offer.query.get(pk)
    db.session.delete(offer_for_delete)
    db.session.commit()
    return 'offer deleted'
