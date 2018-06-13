from flask_restful import Resource
from backend.ext import ma
from flask_jwt_extended import jwt_required
from backend.app.models.vehicle import Vehicle
from flask import request
from sqlalchemy.exc import DBAPIError, OperationalError
import traceback


class VehicleSchema(ma.ModelSchema):
    class Meta:
        model = Vehicle


class VehicleAdd(Resource):
    vehicle_schema = VehicleSchema()

    @classmethod
    def post(cls):

        try:
            json = request.get_json()

            new_vehicle = {
                'year': str(json.get('year')),
                'make': str(json.get('make')),
                'model': str(json.get('model'))
            }

            vehicle = cls.vehicle_schema.loads(new_vehicle).data
            vehicle.save()

            return {'message': 'New vehicle created successfully'}, 201

        except OperationalError or DBAPIError as e:
            print(e.args)

            return {'message': 'Database error. Please contact an admin.'}, 500

        except Exception:
            print(traceback.format_exc())

            return {'message': 'Error with server. Please contact an admin.'}, 500

