from backend.api.models import User
from werkzeug.security import check_password_hash


def test_new_user():
    user = User("test", "password", "test@gmail.com")

    assert user.email == "test@gmail.com"
    assert user.password != "password"
    assert check_password_hash(user.password, "password")
    assert user.username == "test"
