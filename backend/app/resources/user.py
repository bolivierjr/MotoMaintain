from backend.app.models.user import UserModel
from flask_restful import Resource, reqparse


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank")

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        if UserModel.find_by_username(data.get('username')):
            return {'message', 'User already exists'}, 400

        user = UserModel(**data)
        user.save()

        return {'message': 'User created successfully'}, 201
