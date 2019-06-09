import os
from flask import Flask, render_template
from flask_restful import Api
from backend.api.extensions import db, ma, jwt, migrate
from backend.api.controllers import UserRegister, UserLogin, UserLogout, VehicleAdd


basedir = os.path.dirname(__file__)
# static = os.path.join(basedir, "../../dist/static")
# template = os.path.join(basedir, "../../dist")
settings = os.path.join(basedir, "settings.py")


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config.from_pyfile(settings)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(UserRegister, "/api/register")
    api.add_resource(UserLogin, "/api/login")
    api.add_resource(UserLogout, "/api/auth/logout")

    api.add_resource(VehicleAdd, "/api/auth/vehicle")

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        return render_template("index.html")

    return app
