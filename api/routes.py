from fastapi import APIRouter, Request, Response, status, UploadFile, File, Depends
from schemas import *
from fastapi.exceptions import HTTPException
from pydantic import Json
from typing import Annotated
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/api/v1")

@router.post("/"
            #  response_model=EvacuationMapTimeSeries
)
async def start_solve(data: BaseSettings = Depends()):
    
    # image_extensions = ["jpg", "jpeg", "png", "bmp"]
    # extension = image.filename.split(".")[-1]
    # if extension.lower() not in image_extensions:
    #     return HTTPException(status_code=400, detail="Bad filetype")
    
    return data.gases


