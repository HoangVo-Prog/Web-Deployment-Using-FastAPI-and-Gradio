from fastapi import FastAPI

app = FastAPI()

database = [{"id": id, "name": name} for id, name in enumerate(["Alice", "Bob", "Charlie", "David"])]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Path Operations API!"}

@app.get("/database")
def get_database():
    return database

# @app.get("/get_user") # Query using /get_user?user_id=id
@app.get("/get_user/{user_id}") # Path using /get_user/id
def get_user(user_id: int):
    if 0 <= user_id < len(database):
        return database[user_id]
    return {"error": "User not found"}

@app.post("/post_user")
def post_user(name: str):
    new_user = {"id": len(database), "name": name}
    database.append(new_user)
    return new_user

@app.put("/update_user/{user_id}")
def update_user(user_id: int, name: str):
    if 0 <= user_id < len(database):
        database[user_id]["name"] = name
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
