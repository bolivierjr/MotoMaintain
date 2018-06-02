from backend.app import create_app
from backend.db import db
from flask_migrate import Migrate

app = create_app()

migrate = Migrate(app, db)

if __name__ == '__main__':
    db.init_app(app)
    app.run(host='0.0.0.0')
