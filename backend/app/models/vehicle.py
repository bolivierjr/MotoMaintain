from backend.ext import db


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(5), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User")

    def __init__(self, year, make, model, user_id):
        self.year = year
        self.make = make
        self.model = model
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Vehicle {}>".format(self.model)


class Maintenance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
