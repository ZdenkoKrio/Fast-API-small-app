from fastapi import FastAPI
from typing import Optional
from item import Item


app = FastAPI()

fake_items_db = {}


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = fake_items_db.get(item_id)
    if item:
        return {"item_id": item_id, "item": item}

    return {"error": "Item not found"}, 404


@app.post("/items/")
def create_item(item: Item):
    item_id = len(fake_items_db) + 1
    fake_items_db[item_id] = item
    return {"item_id": item_id, "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in fake_items_db:
        fake_items_db[item_id] = item
        return {"item_id": item_id, "item": item}

    return {"error": "Item not found"}, 404
