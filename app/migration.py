import json
import os
from app import db, models
import re
from datetime import datetime


DATE_PATTERN = re.compile(r'\d{2}/\d{2}/\d{4}')


def load_fixture(file_path):
    """
    Загружает данные из фикстуры
    :param file_path:
    :return:
    """
    data = []
    if os.path.isfile(file_path):
        with open(file_path) as file:
            data = json.load(file)

    return data


def migrate_users(fixture_path):
    fixture_data = load_fixture(fixture_path)

    for user in fixture_data:

        if db.session.query(models.User).filter(models.User.id == user['id']).first() is None:
            new_user = models.User(**user)
            db.session.add(new_user)

    db.session.commit()


def migrate_orders(fixture_path):
    fixture_data = load_fixture(fixture_path)

    for order in fixture_data:

        for field_name, filed_value in order.items():
            if isinstance(filed_value, str) and re.search(DATE_PATTERN, filed_value):
                order[field_name] = datetime.strptime(filed_value, '%m/%d/%Y').date()

        if db.session.query(models.Order).filter(models.Order.id == order['id']).first() is None:
            new_order = models.Order(**order)
            db.session.add(new_order)

    db.session.commit()


def migrate_offers(fixture_path):
    fixture_data = load_fixture(fixture_path)

    for offer in fixture_data:

        if db.session.query(models.Offer).filter(models.Offer.id == offer['id']).first() is None:
            new_offer = models.Offer(**offer)
            db.session.add(new_offer)

    db.session.commit()