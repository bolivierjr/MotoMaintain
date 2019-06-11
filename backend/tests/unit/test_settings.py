import backend.api.settings as settings


def test_settings():
    assert settings.JWT_TOKEN_LOCATION == ["cookies"]
    assert settings.JWT_ACCESS_COOKIE_PATH == "/api/auth"
    assert settings.JWT_REFRESH_COOKIE_PATH == "/token/refresh"
    assert settings.JWT_CSRF_IN_COOKIES is True
    assert settings.JWT_COOKIE_CSRF_PROTECT is True
    assert settings.SQLALCHEMY_TRACK_MODIFICATIONS is False
    assert len(settings.SECRET_KEY) >= 32
    assert len(settings.JWT_SECRET_KEY) >= 32
