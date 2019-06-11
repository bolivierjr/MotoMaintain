from backend.api.models import Vehicle, Maintenance


def test_new_vehicle():
    vehicle = Vehicle("1987", "Ford", "Mustang", 1)

    assert vehicle.year == "1987"
    assert vehicle.make == "Ford"
    assert vehicle.model == "Mustang"
    assert vehicle.user_id == 1


def test_new_maintenance():
    maintenance = Maintenance()

    assert maintenance.vehicle_id == 1
