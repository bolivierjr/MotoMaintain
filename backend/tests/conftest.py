import os
import pytest
from backend.api import create_app
from backend.api.extensions import db


@pytest.fixture(scope="session")
def app():
    flask_app = create_app()

    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    flask_app.config["TESTING"] = True
    flask_app.config["JWT_COOKIE_CSRF_PROTECT"] = True
    flask_app.config["JWT_CSRF_IN_COOKIES"] = True

    with flask_app.test_request_context():
        db.create_all()

        yield flask_app

        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as client:
        return client
