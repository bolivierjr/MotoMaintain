import os
import pytest
from backend.api import create_app
from backend.api.ext import db


@pytest.fixture(scope="session")
def app():
    flask_app = create_app()

    flask_app.config["SECRET_KEY"] = "testing"
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
    flask_app.config["TESTING"] = True
    flask_app.config["JWT_SECRET_KEY"] = "dev"
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    flask_app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    flask_app.config["JWT_ACCESS_COOKIE_PATH"] = "/api/auth"
    flask_app.config["JWT_REFRESH_COOKIE_PATH"] = "/token/refresh"
    flask_app.config["JWT_COOKIE_CSRF_PROTECT"] = False
    flask_app.config["JWT_CSRF_IN_COOKIES"] = False

    with flask_app.app_context():
        db.create_all()

        yield flask_app

        db.session.remove()
        db.drop_all()
