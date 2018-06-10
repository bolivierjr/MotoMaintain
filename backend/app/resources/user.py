from backend.app.models.user import UserModel, UserSchema
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from flask import request
from werkzeug.security import check_password_hash


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


class UserLogin(Resource):
    def post(self):
        json = request.get_json()

        user = UserModel.find_by_username(json.get('username'))

        if user:
            password = check_password_hash(user.password, json.get('password'))

            if not password:
                return {'message': 'Invalid Password'}

        else:
            return {'message': 'Invalid Username'}, 401

        if user and password:
            access_token = create_access_token(identity=user.id, fresh=True)

            return {'access_token': access_token}, 200
