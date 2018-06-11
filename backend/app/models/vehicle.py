from backend.db import db, ma


class VehicleModel(db.Model):
    __tablename__= 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(5), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class VehicleSchema(ma.ModelSchema):
    class Meta:
        model = VehicleModel