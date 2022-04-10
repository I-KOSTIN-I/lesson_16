import os.path

DATA_BASE_PATH = os.path.join(os.getcwd(), 'yum_yum.db')
FIXTURE_DIR = 'fixtures'


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATA_BASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USERS_FIXTURE_PATH = os.path.join(FIXTURE_DIR, 'users.json')
    ORDERS_FIXTURE_PATH = os.path.join(FIXTURE_DIR, 'orders.json')
    OFFERS_FIXTURE_PATH = os.path.join(FIXTURE_DIR, 'offers.json')