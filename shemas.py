from pydantic import BaseModel
from fastapi import UploadFile
from enum import Enum


class GasType(Enum):
    test_gas = 0

class Gas(BaseModel):
    gas: GasType
    v: float

    class Config:
        orm_mode = True

class PointType(Enum):
    people = 0
    free_space = 1
    wall = 2
    enter = 3

class Point(BaseModel):
    point: PointType
    gases: list(Gas)

    class Config:
        orm_mode = True

class Field(BaseModel):
    field: list(list(Point))
    
    class Config:
        orm_mode = True

class Person(BaseModel):
    v: float

class Init(BaseModel):
    person: Person
    field: Field



