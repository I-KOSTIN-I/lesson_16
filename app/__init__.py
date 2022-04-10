from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    with app.app_context():
        from app import routes

        db.create_all()

        from app import migration

        migration.migrate_users(app.config['USERS_FIXTURE_PATH'])
        migration.migrate_orders(app.config['ORDERS_FIXTURE_PATH'])
        migration.migrate_offers(app.config['OFFERS_FIXTURE_PATH'])

        return app
