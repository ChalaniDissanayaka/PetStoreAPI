from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from ..init import db
from ..models.petitem import PetItemModel
from ..schemas import PetItemSchema, PetItemUpdateSchema

blp = Blueprint("PetItems", __name__, description="Operations on pet items")


@blp.route("/pet_item/<int:pet_item_id>")
class PetItem(MethodView):
    @jwt_required()
    @blp.response(200, PetItemSchema)
    def get(self, pet_item_id):
        pet_item = PetItemModel.query.get_or_404(pet_item_id)
        return pet_item

    @jwt_required()
    def delete(self, pet_item_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required")

        pet_item = PetItemModel.query.get_or_404(pet_item_id)
        db.session.delete(pet_item)
        db.session.commit()
        return {"message": "Pet Item deleted."}, 200

    @jwt_required()
    @blp.arguments(PetItemUpdateSchema)
    @blp.response(200, PetItemSchema)
    def put(self, pet_item_data, pet_item_id):   # pet_item_data must be before pet_item_id, The URL argument come in at the end. The injected arguments are passed first.
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required")

        pet_item = PetItemModel.query.get(pet_item_id)

        if pet_item:
            pet_item.price = pet_item_data["price"]
            pet_item.item_name = pet_item_data["item_name"]
            pet_item.item_description = pet_item_data["item_description"]
        else:
            pet_item = PetItemModel(id=pet_item_id, **pet_item_data)

        db.session.add(pet_item)
        db.session.commit()

        return pet_item


@blp.route("/pet_item")
class PetItemList(MethodView):
    @jwt_required()
    @blp.response(200, PetItemSchema(many=True))
    def get(self):
        return PetItemModel.query.all()

    @jwt_required()
    @blp.arguments(PetItemSchema)
    @blp.response(201, PetItemSchema)
    def post(self, pet_item_data):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required")

        pet_item = PetItemModel(**pet_item_data)

        try:
            db.session.add(pet_item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the pet item.")

        return pet_item
