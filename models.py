from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import session

db = SQLAlchemy()
migrate = Migrate()

class Member(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    pwd = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)

class Hospital(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    tel = db.Column(db.String(20), nullable=False)

class HospService:
    def addHosp(self, h:Hospital):
        db.session.add(h)
        db.session.commit()

    def getAll(self):
        return Hospital.query.order_by(Hospital.num.asc())