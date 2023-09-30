import os
from schemas import base as base_entity
from api.routes import router

from fastapi import FastAPI, Request, Response, status, UploadFile, File
from fastapi.exceptions import HTTPException

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    pass