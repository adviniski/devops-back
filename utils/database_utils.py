from sqlalchemy_utils import database_exists, create_database
from flask import Flask
from models import *

def create_db():
    if not database_exists(url=instance):
        create_database(url=instance)

def create_tables(app:Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()

def seeds(app:Flask):
    with app.app_context():
        user = User(name="Antonio David Viniski", email="antonio.david@pucpr.br")
        user2 = User(name="João da Silva", email="joao.silva@pupr.br")
        user3 = User(name="Maria de Jesus", email="maria.jesus@pupr.br")
        user4 = User(name="Jorge dos Santos", email="jorge.santos@pupr.br")
        user5 = User(name="Juliana de Andrade", email="juliana.andrade@pupr.br")

        db.session.add_all([user, user2,user3,user4,user5])
        db.session.commit()
