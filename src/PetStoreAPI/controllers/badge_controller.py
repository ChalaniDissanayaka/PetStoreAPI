from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from ..init import db
from ..models.store import StoreModel
from ..models.badge import BadgeModel
from ..models.petitem import PetItemModel

from ..schemas import BadgeSchema
from ..schemas import BadgeAndPetItemSchema

blp = Blueprint("Badges", "badges", description="Operations on badges")


@blp.route("/store/<int:store_id>/badge")
class BadgesInStore(MethodView):
    @jwt_required()
    @blp.response(200, BadgeSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        return store.badges.all()

    @jwt_required()
    @blp.arguments(BadgeSchema)
    @blp.response(201, BadgeSchema)
    def post(self, badge_data, store_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required")

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


@blp.route("/pet_item/<int:pet_item_id>/badge/<int:badge_id>")
class AddBadgesToPetItem(MethodView):
    @jwt_required()
    @blp.response(201, BadgeSchema)
    def post(self, pet_item_id, badge_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required")

        pet_item = PetItemModel.query.get_or_404(pet_item_id)
        badge = BadgeModel.query.get_or_404(badge_id)

        pet_item.badges.append(badge)

        try:
            db.session.add(pet_item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the badge.")

        return badge

    @jwt_required()
    @blp.response(200, BadgeAndPetItemSchema)
    def delete(self, pet_item_id, badge_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required")

        pet_item = PetItemModel.query.get_or_404(pet_item_id)
        badge = BadgeModel.query.get_or_404(badge_id)

        pet_item.badges.remove(badge)

        try:
            db.session.add(pet_item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while deleting the badge.")

        return {"message": "Pet Item removed from the badge", "pet item": pet_item, "badge": badge}


@blp.route("/badge/<int:badge_id>")
class Badge(MethodView):
    @jwt_required()
    @blp.response(200, BadgeSchema)
    def get(self, badge_id):
        badge = BadgeModel.query.get_or_404(badge_id)
        return badge

    @jwt_required()
    @blp.response(
        202,
        description="Deletes a badge if no pet item is attached with it.",
        example={"message": "Badge deleted."},
    )
    @blp.alt_response(404, description="Badge not found.")
    @blp.alt_response(
        400,
        description="Returned if the badge is assigned to one or more pet items. In this scenario, the badge is not deleted.",
    )
    def delete(self, badge_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required")

        badge = BadgeModel.query.get_or_404(badge_id)

        if not badge.petitems:
            db.session.delete(badge)
            db.session.commit()
            return {"message": "Badge deleted."}
        abort(
            400,
            message="Could not delete badge. Make sure badge is not attached with any pet items, then try again.",
        )
