import json
from PIL import Image
from io import BytesIO
from pydantic import BaseModel, validator
from typing import List, Optional
from enum import Enum
from fastapi import FastAPI, Form, UploadFile, File

class Pos(BaseModel):
    x: int
    y: int

class GasType(Enum):
    test_gas = 0


class Gas(BaseModel):
    pos: Pos
    gas_type: GasType

    def velocity(self) -> float:
        pass

class Person(BaseModel):
    pos: Pos
    velocity: float = 1.0

class Destination(BaseModel):
    position: Pos

class BaseElement(Enum):
    free = 0
    wall = 1
    person = 2
    gas = 3

class EvacuationMap(BaseModel):
    ev_map: List[List[BaseElement]]
    def pprint(self):
        for i in range(len(self.ev_map)):
            row = ""
            for j in range(len(self.ev_map[i])):
                row += f"{self.ev_map[i][j].value} "
            print(row)

class EvacuationMapTimeSeries(BaseModel):
    maps_series: List[EvacuationMap]

    def pprint(self):
        for t in range(len(self.maps_series)):
            print(t)
            self.maps_series[t].pprint()

class BaseSettings(BaseModel):
    person: Person = Form(...)
    gases: List[Gas] = Form(...)
    evacuation_map: EvacuationMap = Form(...)

    class Config:
        from_attributes = True
