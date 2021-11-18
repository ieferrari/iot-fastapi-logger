from fastapi import APIRouter, Form, Depends, HTTPException
from ..schemas.users import UserCreate, UserBase, User
from ..schemas.sensors import Sensor
from ..dependencies.deps import get_db
from ..crud.users import user_already_exists, create_new_user
from ..crud.sensors import get_sensors_for_user
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/sensor/", tags=["sensors"])  # response_model=Sensor)
async def get_sensors_for_user(username: str, db: Session = Depends(get_db)):
    return get_sensors_for_user(db=db, username=username)
    # return {"get_sensors_for_user": username}
