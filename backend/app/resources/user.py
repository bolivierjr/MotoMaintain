from backend.app.models.user import UserModel, UserSchema
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask import request
from werkzeug.security import check_password_hash
from sqlalchemy.exc import DBAPIError, OperationalError


class UserRegister(Resource):
    user_schema = UserSchema()

    @classmethod
    def post(cls):
        """
        Post method to create/register a User and save in the database.
        Return proper JSON response back from the API given the parameters.
        """

        try:
            json = request.get_json()
            username = str(json.get('username'))
            password = str(json.get('password'))
            email = str(json.get('email'))

            new_user = {
                'username': username,
                'password': password,
                'email': email
            }

            if not username or not password or not email:
                return {'message': 'Fields must not be blank'}, 400

            elif UserModel.find_by_username(username):
                return {'message': 'Username already exists'}, 400

            elif UserModel.find_by_email(email):
                return {'message': 'Email already exists'}, 400

            user = cls.user_schema.load(**new_user).data
            user.save()

            return {'message': 'User created successfully'}, 201

        except OperationalError or DBAPIError as e:
            print(e.args)

            return {'message': 'Database error. Please contact an admin.'}, 500

        except Exception as e:
            print(e.args)

            return {'message': 'Error with server. Please contact an admin.'}


class UserLogin(Resource):
    def post(self):
        try:
            json = request.get_json()

            user = UserModel.find_by_username(str(json.get('username')))

            if user:
                password = check_password_hash(
                    user.password, str(json.get('password')))

                if not password:
                    return {'message': 'Invalid Password'}

            else:
                return {'message': 'Invalid Username'}, 401

            if user and password:
                access_token = create_access_token(identity=user.id, fresh=True)

                return {'access_token': access_token}, 200

        except OperationalError or DBAPIError as e:
            print(e.args)

            return {'message': 'Database error. Please contact an admin.'}, 500

        except Exception as e:
            print(e.args)

            return {'message': 'Error with server. Please contact ad admin.'}, 500