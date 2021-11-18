from fastapi import APIRouter, Form, Depends, HTTPException
from ..schemas.users import UserCreate, UserBase, User
from ..dependencies.deps import get_db
from ..crud.users  import user_already_exists, create_new_user, get_users
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/users/", response_model=User)
async def get_all_users(db: Session = Depends(get_db)):
    return get_users(db=db)


@router.post("/users/", response_model=User)
async def create_user(username: str = Form(...),
                      email: str = Form(...),
                      password: str = Form(...),
                      db: Session = Depends(get_db)):
    db_user = user_already_exists(db, username=username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    user_schema = UserCreate(password=password, email=email, username=username)
    return create_new_user(db=db, user=user_schema)


@router.get("/users/{username}", tags=["extra"])
async def read_user(username: str):
    return {"username": username}
