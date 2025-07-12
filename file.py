from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(upload_file: Annotated[UploadFile, File()]):
    contents = await upload_file.read()
    return {
        "filename": upload_file.filename,
        "file_size": len(contents), 
        "content_type": upload_file.content_type}