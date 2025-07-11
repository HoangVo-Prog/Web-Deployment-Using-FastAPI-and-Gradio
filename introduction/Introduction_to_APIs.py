# How to run

# uvicorn Introduction_to_APIs:app --reload
# open http://127.0.0.1:8000/docs
# Ctrl + C to stop the server


from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get("/")
def read_root():
    time.sleep(2)
    return {"message": "Hello, FastAPI!"}

# Avoid use time.sleep in async function, it will block the event loop, instead use asyncio.sleep
# Avoid using @app.get("/") 2 times, the second one will override the first one

@app.get("/")
async def read_root():
    await asyncio.sleep(2)
    return {"message": "Done"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)