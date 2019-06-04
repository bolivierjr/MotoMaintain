from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError
from backend.api.models.user import User, UserSchema
from werkzeug.security import check_password_hash
from sqlalchemy.exc import DBAPIError, OperationalError
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    jwt_required,
)


class UserRegister(Resource):
    def post(self):
        """
        Post method to create/register a User and save in the database.
        Return proper JSON response back from the API given the parameters.
        """
        try:
            UserSerializer = UserSchema(strict=True)
            new_user_data = UserSerializer.loads(request.data).data

            username = new_user_data.get("username")
            email = new_user_data.get("email")

            if User.find_by_username(username):
                return {"message": "Username already exists"}, 400

            elif User.find_by_email(email):
                return {"message": "Email already exists"}, 400

            user = User(**new_user_data)
            user.save()

            return {"message": "User created successfully"}, 201
        
        except ValidationError as err:
            return {"message": err.messages}, 422

        except (OperationalError, DBAPIError) as err:
            print(err.args)

            return {"message": "Database error. Please contact an admin."}, 500

        except Exception as err:
            print(err.args)

            return {"message": "Error with server. Please contact an admin."}, 500


class UserLogin(Resource):
    def post(self):
        try:
            UserSerializer = UserSchema(strict=True)
            user_data = UserSerializer.loads(request.data, partial=('email',)).data

            user = User.find_by_username(user_data.get("username"))

            if user:
                password = check_password_hash(
                    user.password,
                    user_data.get("password")
                )

                if not password:
                    return {"message": "Invalid Password"}, 401

            else:
                return {"message": "Invalid Username"}, 401

            if user and password:
                access_token = create_access_token(
                    identity=user.id,
                    fresh=True
                )
                refresh_token = create_refresh_token(identity=user.id)

                response = jsonify({"logged_in": True})
                response.status_code = 200

                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)

                return response

        except ValidationError as err:
            return {"message": err.messages}, 422

        except (OperationalError, DBAPIError) as err:
            print(err.args)

            return {"message": "Database error. Please contact an admin."}, 500

        except Exception as err:
            print(err.args)

            return {"message": "Error with server. Please contact an admin."}, 500


class UserLogout(Resource):
    @jwt_required
    def post(self):
        response = jsonify({"logged_in": False})
        response.status_code = 200
        unset_jwt_cookies(response)

        return response
