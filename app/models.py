from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
        db.metadata.create_all(engine)
        db.session.commit()
    return engine


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(30), nullable=False)
    brand = db.Column(db.String(30), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    category = db.Column(db.String(30), nullable=False)



