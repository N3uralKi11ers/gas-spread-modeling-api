from fastapi import APIRouter, Request, Response, status, UploadFile, File, Depends
from schemas import *
from fastapi.exceptions import HTTPException
from fastapi import Form
from dataclasses import dataclass

router = APIRouter(prefix="/api/v1")

@dataclass
class SimpleModel:
    no: int = Form(...)
    nm: str = Form(...)
    UploadFile = Form(...)


@router.post("/form")
def form_post(form_data: SimpleModel = Depends()):
    return form_data

@router.post("/", 
            #  response_model=EvacuationMapTimeSeries
)
def start_solve(settings: BaseSettings = FormObject(...), image: UploadFile = File(...)):
    image_extensions = ["jpg", "jpeg", "png", "bmp"]
    extension = image.filename.split(".")[-1]
    if extension.lower() not in image_extensions:
        return HTTPException(status_code=400, detail="Bad filetype")
    
    return EvacuationMapTimeSeries()


