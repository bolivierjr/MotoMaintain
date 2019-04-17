import os
from flask import Flask, render_template
from flask_restful import Api
from backend.ext import db, jwt, migrate
from backend.app.resources.user import UserRegister, UserLogin, UserLogout
from backend.app.resources.vehicle import VehicleAdd

basedir = os.path.dirname(__file__)
static = os.path.join(basedir, "../../dist/static")
template = os.path.join(basedir, "../../dist")
settings = os.path.join(basedir, "../settings.py")


def create_app():
    app = Flask(__name__, static_folder=static, template_folder=template)
    api = Api(app)

    app.config.from_pyfile(settings)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")
    api.add_resource(UserLogout, "/logout")
    api.add_resource(VehicleAdd, "/vehicle/add")

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        return render_template("index.html")

    return app
