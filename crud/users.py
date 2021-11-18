from sqlalchemy.orm import Session
from ..models import users
from .. import schemas


def get_users(db: Session):
    return db.query(users.User)


def user_already_exists(db: Session, username: str) -> bool:
    return db.query(users.User).filter(users.User.username == username).first()


def create_new_user(db: Session, user: schemas.users.UserCreate):
    fake_hashed = user.password + "not_hased"
    db_user = users.User(email=user.email,
                         username=user.username,
                         hashed_password=fake_hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
