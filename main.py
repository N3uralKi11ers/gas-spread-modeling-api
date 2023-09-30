import os
import shemas

from fastapi import FastAPI, Request, Response, status, UploadFile, File

app = FastAPI()

@app.post("/init/")
async def create_init(init: shemas.Init, image: UploadFile = File(...)):
    # Обработка запроса
    return {"init": init, "image_name": image.filename}

