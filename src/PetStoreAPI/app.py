from flask import Flask, request
from db import stores, pet_items
import uuid

app = Flask(__name__)


@app.get("/store")  # GET http://127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")  # POST http://127.0.0.1:5000/store
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store

    return store, 201


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Pet Store not found"}, 404


@app.post("/pet_item")  # POST http://127.0.0.1:5000/pet_item
def create_pet_item():
    pet_item_data = request.get_json()
    if pet_item_data["store_id"] not in stores:
        return {"message": "Pet Store not found"}, 404

    item_id = uuid.uuid4().hex
    pet_item = {**pet_item_data, "id": item_id}
    pet_items[item_id] = pet_item

    return pet_item, 201


@app.get("/pet_item")
def get_all_pet_items():
    return {"pet_items": list(pet_items.values())}


@app.get("/pet_item/<string:pet_item_id>")
def get_pet_item(pet_item_id):
    try:
        return pet_items[pet_item_id]
    except KeyError:
        return {"message": "Pet Item not found"}, 404
