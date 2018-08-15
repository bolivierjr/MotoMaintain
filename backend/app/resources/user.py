from flask_restful import Resource
from flask import request, jsonify
from backend.app.models.user import User
from werkzeug.security import check_password_hash
from sqlalchemy.exc import DBAPIError, OperationalError
from flask_jwt_extended import (create_access_token, set_access_cookies,
                                unset_jwt_cookies, jwt_required)


class UserRegister(Resource):
    def post(self):
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

            elif User.find_by_username(username):
                return {'message': 'Username already exists'}, 400

            elif User.find_by_email(email):
                return {'message': 'Email already exists'}, 400

            user = User(**new_user)
            user.save()

            return {'message': 'User created successfully'}, 201

        except OperationalError or DBAPIError as e:
            print(e.args)

            return {'message': 'Database error. Please contact an admin.'}, 500

        except Exception as e:
            print(e.args)

            return {'message': 'Error with server. Please contact an admin.'}, 500


class UserLogin(Resource):
    def post(self):
        try:
            json = request.get_json()

            user = User.find_by_username(str(json.get('username')))

            if user:
                password = check_password_hash(
                    user.password, str(json.get('password')))

                if not password:
                    return {'message': 'Invalid Password'}

            else:
                return {'message': 'Invalid Username'}, 401

            if user and password:
                access_token = create_access_token(identity=user.id, fresh=True)

                response = jsonify({'logged_in': True})
                response.status_code = 200

                set_access_cookies(response, access_token)
                return response

        except OperationalError or DBAPIError as e:
            print(e.args)

            return {'message': 'Database error. Please contact an admin.'}, 500

        except Exception as e:
            print(e.args)

            return {'message': 'Error with server. Please contact an admin.'}, 500


class UserLogout(Resource):
    @jwt_required
    def post(self):
        response = jsonify({'logged_in': False})
        response.status_code = 200
        unset_jwt_cookies(response)

        return response

