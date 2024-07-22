from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from ..init import db
from ..models.store import StoreModel
from ..models.badge import BadgeModel
from ..schemas import BadgeSchema

blp = Blueprint("Badges", "badges", description="Operations on badges")


@blp.route("/store/<string:store_id>/badge")
class BadgesInStore(MethodView):
    @blp.response(200, BadgeSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        return store.badges.all()

    @blp.arguments(BadgeSchema)
    @blp.response(201, BadgeSchema)
    def post(self, badge_data, store_id):
        if BadgeModel.query.filter(BadgeModel.store_id == store_id, BadgeModel.badge_name == badge_data["badge_name"]).first():
            abort(400, message="A badge with the provided name already exists in the pet store.")

        badge = BadgeModel(**badge_data, store_id=store_id)

        try:
            db.session.add(badge)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(
                500,
                message=str(e),
            )

        return badge


@blp.route("/badge/<string:badge_id>")
class Badge(MethodView):
    @blp.response(200, BadgeSchema)
    def get(self, badge_id):
        badge = BadgeModel.query.get_or_404(badge_id)
        return badge
