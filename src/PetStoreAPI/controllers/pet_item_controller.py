import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from .db import pet_items
from .schemas import PetItemSchema, PetItemUpdateSchema

blp = Blueprint("PetItems", __name__, description="Operations on pet items")


@blp.route("/pet_item/<string:pet_item_id>")
class PetItem(MethodView):
    @blp.response(200, PetItemSchema)
    def get(self, pet_item_id):
        try:
            return pet_items[pet_item_id]
        except KeyError:
            abort(404, message="Pet Item not found.")

    def delete(self, pet_item_id):
        try:
            del pet_items[pet_item_id]
            return {"message": "Pet Item deleted."}
        except KeyError:
            abort(404, message="Pet Item not found.")

    @blp.arguments(PetItemUpdateSchema)
    @blp.response(200, PetItemSchema)
    def put(self, pet_item_data, pet_item_id):   # pet_item_data must be before pet_item_id, The URL argument come in at the end. The injected arguments are passed first.
        try:
            pet_item = pet_items[pet_item_id]
            pet_item |= pet_item_data  # |= update operator

            return pet_item
        except KeyError:
            abort(404, message="Pet Item not found.")


@blp.route("/pet_item")
class PetItemList(MethodView):
    @blp.response(200, PetItemSchema(many=True))
    def get(self):
        return pet_items.values()

    @blp.arguments(PetItemSchema)
    @blp.response(201, PetItemSchema)
    def post(self, pet_item_data):
        for pet_item in pet_items.values():
            if (
                pet_item_data["item_name"] == pet_item["item_name"]
                and pet_item_data["store_id"] == pet_item["store_id"]
            ):
                abort(400, message=f"Pet Item already exists.")

        item_id = uuid.uuid4().hex
        pet_item = {**pet_item_data, "id": item_id}
        pet_items[item_id] = pet_item

        return pet_item
