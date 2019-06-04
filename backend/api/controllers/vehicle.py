from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.api.models.vehicle import Vehicle
from sqlalchemy.exc import DBAPIError, OperationalError
import traceback


class VehicleAdd(Resource):
    @jwt_required
    def post(self):

        try:
            json = request.get_json()

            new_vehicle = {
                "year": str(json.get("year")),
                "make": str(json.get("make")),
                "model": str(json.get("model")),
                "user_id": get_jwt_identity(),
            }

            vehicle = Vehicle(**new_vehicle)
            vehicle.save()

            return {"message": "New vehicle created successfully"}, 201

        except (OperationalError, DBAPIError) as err:
            print(err.args)

            return {"message": "Database error. Please contact an admin."}, 500

        except Exception:
            print(traceback.format_exc())

            return {"message": "Error with server. Please contact an admin."}, 500
