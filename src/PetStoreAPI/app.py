from flask import Flask, request
from db import stores, pet_items
from flask_smorest import abort
import uuid

app = Flask(__name__)


@app.get("/store")  # GET http://127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")  # POST http://127.0.0.1:5000/store
def create_store():
    store_data = request.get_json()

    if "store_name" not in store_data:
        abort(
            400,
            message="Bad request. Ensure 'store_name' is included in the JSON payload.",
        )
    for store in stores.values():
        if store_data["store_name"] == store["store_name"]:
            abort(400, message=f"Pet Store already exists.")

    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Pet Store not found.")


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Pet Store deleted."}
    except KeyError:
        abort(404, message="Pet Store not found.")


@app.post("/pet_item")  # POST http://127.0.0.1:5000/pet_item
def create_pet_item():
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


@app.get("/pet_item")
def get_all_pet_items():
    return {"pet_items": list(pet_items.values())}


@app.get("/pet_item/<string:pet_item_id>")
def get_pet_item(pet_item_id):
    try:
        return pet_items[pet_item_id]
    except KeyError:
        abort(404, message="Pet Item not found.")


@app.delete("/pet_item/<string:pet_item_id>")
def delete_pet_item(pet_item_id):
    try:
        del pet_items[pet_item_id]
        return {"message": "Pet Item deleted."}
    except KeyError:
        abort(404, message="Pet Item not found.")


@app.put("/pet_item/<string:pet_item_id>")
def update_pet_item(pet_item_id):
    pet_item_data = request.get_json()

    if "price" not in pet_item_data or "item_name" not in pet_item_data:
        abort(
            400,
            message="Bad request. Ensure 'price', and 'item_name' are included in the JSON payload.",
        )
    try:
        pet_item = pet_items[pet_item_id]
        pet_item |= pet_item_data

        return pet_item
    except KeyError:
        abort(404, message="Pet Item not found.")
