from pydantic import BaseModel
from fastapi import UploadFile
from enum import Enum
from typing import List

class GasType(Enum):
    test_gas = 0

class Gas(BaseModel):
    gas: GasType
    v: float

    class Config:
        from_attributes = True

class PointType(Enum):
    people = 0
    free_space = 1
    wall = 2
    enter = 3

class Point(BaseModel):
    point: PointType
    gases: List[Gas]

    class Config:
        from_attributes = True

class Field(BaseModel):
    field: List[List[Point]]
    
    class Config:
        from_attributes = True

class Person(BaseModel):
    v: float

    class Config:
        from_attributes = True

class Marker(BaseModel):
    place: Point
    x: float
    y: float

    class Config:
        from_attributes = True

class Init(BaseModel):
    person: Person
    markers: List[Marker]

    class Config:
        from_attributes = True



