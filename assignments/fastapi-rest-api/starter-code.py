from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    in_stock: bool = True

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {
        "item_id": item_id,
        "q": q,
        "name": "Sample Item",
        "price": 9.99,
    }

@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item,
    }
