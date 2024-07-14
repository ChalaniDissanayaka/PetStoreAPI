import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from .db import pet_items

blp = Blueprint("PetItems", __name__, description="Operations on pet items")


@blp.route("/pet_item/<string:pet_item_id>")
class PetItem(MethodView):
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

    def put(self, pet_item_id):
        pet_item_data = request.get_json()

        if "price" not in pet_item_data or "item_name" not in pet_item_data:
            abort(
                400,
                message="Bad request. Ensure 'price' and 'item_name' are included in the JSON payload.",
            )
        try:
            pet_item = pet_items[pet_item_id]
            pet_item |= pet_item_data

            return pet_item
        except KeyError:
            abort(404, message="Pet Item not found.")


@blp.route("/pet_item")
class PetItemList(MethodView):
    def get(self):
        return {"pet_items": list(pet_items.values())}

    def post(self):
        pet_item_data = request.get_json()

        if (
            "price" not in pet_item_data
            or "store_id" not in pet_item_data
            or "item_name" not in pet_item_data
            or "item_description" not in pet_item_data
        ):
            abort(
                400,
                message="Bad request. Ensure 'price', 'store_id', 'item_name' and 'item_description' are included in the JSON payload.",
            )
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
