from backend.api.models import User
from werkzeug.security import check_password_hash


# Assertion helper function to test the user model
def assert_user(user):
    assert user is not None
    assert user.email == "test@gmail.com"
    assert user.password != "password"
    assert check_password_hash(user.password, "password")
    assert user.username == "test"
    assert user.id == 2
    assert repr(user) == "<User test>"


def test_save_user():
    user = User("test", "password", "test@gmail.com")
    user.save()

    assert_user(user)


def test_find_by_email():
    user = User.find_by_email("test@gmail.com")

    assert_user(user)


def test_find_by_username():
    user = User.find_by_username("test")

    assert_user(user)


def test_find_user_by_id():
    user = User.find_by_id(2)

    assert_user(user)


def test_delete_user():
    user = User.find_by_username("test")
    user.delete()

    user = User.find_by_username("test")

    assert user is None
