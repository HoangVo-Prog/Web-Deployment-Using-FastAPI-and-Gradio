from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemFull(BaseModel):
    name: str
    price: float
    secret_code: str

class ItemPublic(BaseModel):
    name: str
    price: float

@app.get("/items/", response_model=ItemPublic)
async def read_item() -> ItemFull:
    return ItemFull(name="Book", price=10, secret_code="topsecret")

# This endpoint returns a full item model, but only the public fields are shown in the response.