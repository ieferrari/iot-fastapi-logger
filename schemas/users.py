from typing import List, Optional
from pydantic import BaseModel
from .sensors import Sensor


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    email: Optional[str] = None


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    sensors: List[Sensor] = []

    class Config:
        orm_mode = True
