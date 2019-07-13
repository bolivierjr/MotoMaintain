from backend.api.extensions import db, ma


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
        return f"<Vehicle {self.model}>"


class Maintenance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"))
    vehicle = db.relationship("Vehicle")

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id


class VehicleSchema(ma.ModelSchema):
    class meta:
        model = Vehicle


class MaintenanceSchema(ma.ModelSchema):
    class meta:
        model = Maintenance
