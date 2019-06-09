def test_register_user(app):
    with app.test_client() as client:
        response = client.post(
            "/api/register",
            json={
                "username": "john",
                "password": "password",
                "email": "john@gmail.com",
            },
            headers={"ContentType": "application/json"},
        )

        assert response.status_code == 201


def test_valid_login(app):
    with app.test_client() as client:
        response = client.post(
            "/api/login",
            json={"username": "john", "password": "password"},
            headers={"ContentType": "application/json"},
        )

        assert response.status_code == 200
