from backend.app.models.user import UserModel, UserSchema
from flask_restful import Resource, reqparse
from flask import request


class UserRegister(Resource):
    user_schema = UserSchema()

    @classmethod
    def post(cls):
        """
        Post method to create/register a User and save in the database.
        Return proper JSON response back from the API given the parameters.
        """

        json = request.get_json()

        if UserModel.find_by_username(json.get('username')):
            return {'message': 'Username already exists'}, 400

        elif UserModel.find_by_email(json.get('email')):
            return {'message': 'Email already exists'}, 400

        user = cls.user_schema.load(json).data
        user.save()

        return {'message': 'User created successfully'}, 201
