import os
from redis import StrictRedis


class JWTRevoke:
    def __init__(self):
        self._credentials = {
            "host": os.getenv("REDIS_HOST"),
            "port": os.getenv("REDIS_PORT"),
            "password": os.get("REDIS_PASSWORD"),
        }
        self.cache = StrictRedis(**self._credentials)
