from sqlalchemy.orm import Session
from ..models  import users, sensors
from .. import routers
from .. import schemas


def get_sensors_for_user(db: Session, username: str):
    user_id = db.query(users.User).filter(users.User.username == username).first().id
    print(user_id)
    return db.query(sensors.Sensor).filter(sensors.Sensor.username==username).first()
