from typing import List
from pydantic import BaseModel
from datetime import datetime


class RegistryBase(BaseModel):
    value: float
    datetime: datetime


class RegistryCreate(RegistryBase):
    sensor_id: int


class Registry(RegistryBase):
    pass


# =============================================================================
class SensorBase(BaseModel):
    label: str


class SensorCreate(SensorBase):
    owner: int


class Sensor(SensorBase):
    id: int
    registries: List[Registry] = []

    class Config:
        orm_mode = True
