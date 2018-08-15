from backend.app.models.user import User
from backend.app.models.vehicle import Vehicle
from backend.app.models.vehicle import Maintenance
from werkzeug.security import check_password_hash

def test_new_user():
    user = User('test', 'password', 'test@gmail.com')

    assert user.email == 'test@gmail.com'
    assert user.password != 'password'
    assert check_password_hash(user.password, 'password')
    assert user.username == 'test'


def test_new_vehicle():
    vehicle = Vehicle('1987', 'Ford', 'Mustang', 1)

    assert vehicle.year == '1987'
    assert vehicle.make == 'Ford'
    assert vehicle.model == 'Mustang'
    assert vehicle.user_id == 1

def test_new_maintenance():
    maintenance = Maintenance()
