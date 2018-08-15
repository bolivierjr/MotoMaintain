import os
import pytest
from backend.app import create_app
from backend.ext import db
from backend.app.models.user import User

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    flask_app.config['SECRET_KEY'] = 'dev'
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:killarmy@localhost/test_db"
    flask_app.config['TESTING'] = True
    flask_app.config['JWT_SECRET_KEY'] = 'dev'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    flask_app.config['JWT_ACCESS_COOKIE_PATH'] = '/login'
    flask_app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    flask_app.config['JWT_CSRF_IN_COOKIES'] = False

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_db():
    db.create_all()

    user1 = User(username='eck0',
                 password='password',
                 email='bolivierjr@gmail.com')

    db.session.add(user1)
    db.session.commit()

    yield db

    db.drop_all()