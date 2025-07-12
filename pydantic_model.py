from pydantic import BaseModel 
from typing import Optional, List, Dict
from fastapi import FastAPI

class User(BaseModel):
    id: int | None = None 
    name: str | None = None
    age: Optional[int] = None
    email: Optional[str] = None
    tag: List[str] = []
    
database = [{"id": id, "name": name} for id, name in enumerate(["Alice", "Bob", "Charlie", "David"])]
user_database = [User(**user) for user in database]
    
app = FastAPI()

@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to the Path Operations API!"}

@app.get("/user_database")
async def get_database():
    return user_database

@app.get("/get_user/{user_id}") 
async def get_user(user_id: int, response_model=User):
    for u in user_database:
        if u.id == user_id:
            return u
    return {"error": "User not found"}

@app.post("/post_user")
async def post_user(user: User):
    if user not in user_database:
        user_database.append(user)
    return user

@app.put("/update_user/{user_id}")
def update_user(user_id: int, user: User):
    if 0 <= user_id < len(database):
        for u in user_database:
            if u.id == user_id:
                u = user
                break
        return database[user_id]
    return {"error": "User not found"}

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    if not (0 <= user_id < len(database)):
        return {"error": "User not found"}
    
    deleted_user = database.pop(user_id)
    for i in range(user_id, len(database)):
        database[i]["id"] -= 1
    return f"{deleted_user['name']} has been deleted"
