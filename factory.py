from flask import Flask
from flask_migrate import Migrate

from api.rest import users

from conf.database import db, bcrypt, Config


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.register_blueprint(users.USER_BLUEPRINT)
    db.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)
    with app.app_context():
        db.create_all()
    return app
