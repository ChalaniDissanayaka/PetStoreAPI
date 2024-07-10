from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "store_name": "Pet Store",
        "store_location": "Knox",
        "pet_items": [
            {
                "item_name": "Dog belt",
                "item_description": "German Shepherd belt",
                "price": 35.50
            },
            {
                "item_name": "Bird feeder",
                "item_description": "Bird feeding station",
                "price": 45.70
            }
        ]
    }
]


@app.get("/store")  # GET http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}


@app.post("/store")  # POST http://127.0.0.1:5000/store
def create_store():
    request_data = request.get_json()
    new_store = {"store_name": request_data["store_name"],
                 "store_location": request_data["store_location"],
                 "pet_items": [{
                     "item_name": "Cat food",
                     "item_description": "Premium quality",
                     "price": 55.20
                 }]}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:store_name>/pet_item")
def create_pet_item(store_name):
    request_data = request.get_json()
    for store in stores:
        if store["store_name"] == store_name:
            new_item = {"item_name": request_data["item_name"], "price": request_data["price"]}
            store["pet_items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:store_name>")
def get_store(store_name):
    for store in stores:
        if store["store_name"] == store_name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:store_name>/pet_item")
def get_pet_item_in_store(store_name):
    for store in stores:
        if store["store_name"] == store_name:
            return {"pet_items": store["pet_items"],
                    "badge_colour_code": "green"}
    return {"message": "Store not found"}, 404
