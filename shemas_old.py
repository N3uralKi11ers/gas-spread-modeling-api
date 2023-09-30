from pydantic import BaseModel
from fastapi import UploadFile
from enum import Enum
from typing import List

class Person(BaseModel):
    velocity: float

    class Config:
        from_attributes = True

class GasType(Enum):
    test_gas = 0

    class Config:
        from_attributes = True

class Gas(BaseModel):
    gas: GasType

    def velocity(self) -> float:
        pass

    class Config:
        from_attributes = True


class Point(BaseModel):
    person: Person
    wall: bool
    enter: bool
    gases: List[Gas]

    class Config:
        from_attributes = True

class EvacuationMap(BaseModel):
    field: List[List[Point]]
    
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



