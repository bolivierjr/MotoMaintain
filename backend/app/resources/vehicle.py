from flask_restful import Resource
from flask_jwt_extended import jwt_required
from backend.app.models.vehicle import VehicleModel, VehicleSchema
from flask import request
from sqlalchemy.exc import DBAPIError, OperationalError


class VehicleAdd(Resource):
    vehicle_schema = VehicleSchema()

    @classmethod
    def post(cls):

        try:
            json = request.get_json()

            new_vehicle = {
                'year': json.get('year'),
                'make': json.get('make'),
                'model': json.get('model')
            }

            vehicle = cls.vehicle_schema.load(**new_vehicle).data
            vehicle.save()

            return {'message': 'New vehicle created successfully'}, 201

        except OperationalError or DBAPIError as e:
            print(e.args)

            return {'message': 'Database error. Please contact an admin.'}, 500

        except Exception as e:
            print(e.args)

            return {'message': 'Error with server. Please contact an admin.'}

