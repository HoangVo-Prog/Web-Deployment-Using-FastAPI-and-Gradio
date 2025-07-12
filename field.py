from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field 

app = FastAPI()

items = [
    {
        "name": "Banh thap cam", 
        "price": 45.0, 
        "description": "A traditional Vietnamese dish with a variety of ingredients.",
    }, 
    {
        "name": "Pho", 
        "price": 50.0, 
        "description": "A popular Vietnamese noodle soup consisting of broth, rice noodles, herbs, and meat.",
    },   
]

class Item(BaseModel):
    name: str = Field(..., title="The name of the item", max_length=50)
    price: float = Field(..., gt=0, description="The price of the item in USD")
    description: str = Field(None, max_length=200, description="A brief description of the item")
    
@app.get("/search_items/")
async def search_items(
    q: Annotated[str, Query(min_length=3, max_length=50, description="Search query for item names")],
    max_price: Annotated[float | None, Query(gt=0, description="Maximum price of items to return")] = None
):
    results = [item for item in items if q.lower() in item["name"].lower()]
    if max_price is not None:
        results = [item for item in results if item["price"] <= max_price]
    return results