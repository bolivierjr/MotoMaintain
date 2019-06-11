from flask import session


def test_valid_register_user(app):
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
        assert response.json["message"] == "User created successfully"
        assert response.headers["Content-Type"] == "application/json"


def test_valid_login(client):
    # with app.test_client() as client:
    login_response = client.post(
        "/api/login",
        json={"username": "john", "password": "password"},
        headers={"Content-Type": "application/json"},
    )

    cookies = login_response.headers.getlist("Set-Cookie")

    csrf_access_result = [
        token.split(" ")[0] for token in cookies if "csrf_access_token" in token
    ][0]

    csrf_refresh_result = [
        token.split(" ")[0] for token in cookies if "csrf_refresh_token" in token
    ][0]

    assert csrf_access_result
    assert csrf_refresh_result
    assert any("access_token_cookie" in cookie for cookie in cookies)
    assert any("refresh_token_cookie" in cookie for cookie in cookies)

    assert login_response.status_code == 200
    assert login_response.json["logged_in"] is True
    assert login_response.headers["Content-Type"] == "application/json"

    # Storing the csrf token in a session to use later for logging out
    with client.session_transaction() as sess:
        _, csrf_access_token = csrf_access_result.split("=")
        _, csrf_refresh_token = csrf_access_result.split("=")
        sess["csrf_access_token"] = csrf_access_token.replace(";", "")
        sess["csrf_refresh_token"] = csrf_refresh_token.replace(";", "")


def test_valid_revoke_access_logout(client):
    with client.session_transaction() as sess:
        # Testing the jwt token revoking/logout endpoints
        revoke_access_response = client.delete(
            "/api/auth/revoke_access",
            headers={
                "Content-Type": "application/json",
                "X-CSRF-TOKEN": sess["csrf_access_token"],
            },
        )

        assert revoke_access_response.status_code == 200
        assert revoke_access_response.json["logged_in"] is False


def test_valid_revoke_refresh_logout(client):
    with client.session_transaction() as sess:
        revoke_refresh_response = client.delete(
            "/api/auth/revoke_refresh",
            headers={
                "Content-Type": "application/json",
                "X-CSRF-TOKEN": sess["csrf_refresh_token"],
            },
        )

        assert revoke_refresh_response.status_code == 200
        assert revoke_refresh_response.json["logged_in"] is False
