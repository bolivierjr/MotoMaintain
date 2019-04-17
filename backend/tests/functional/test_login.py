import json


def test_valid_login_logout(test_client, init_db):
    response = test_client.post(
        "/login",
        data=json.dumps({"username": "eck0", "password": "password"}),
        headers={"ContentType": "application/json"},
    )

    assert response.status_code == 200
