from sqlalchemy_utils import database_exists, create_database
from flask import Flask
from models import *

def create_db():
    if not database_exists(url=instance):
        create_database(url=instance)

def create_tables(app:Flask):
    with app.app_context():
        db.create_all()
        user = User(name="Antonio", email="antonio")
        user2 = User(name="Fernando", email="fernando")

        db.session.add_all([user, user2])
        db.session.commit()
