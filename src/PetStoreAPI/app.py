import os

from flask import Flask
from flask_smorest import Api

from .models.petitem import PetItemModel
from .models.store import StoreModel
from .models.badge import BadgeModel

from .init import db

from .controllers.pet_item_controller import blp as PetItemBlueprint
from .controllers.store_controller import blp as StoreBlueprint
from .controllers.badge_controller import blp as BadgeBlueprint


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Pet Store REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(PetItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(BadgeBlueprint)

    return app
