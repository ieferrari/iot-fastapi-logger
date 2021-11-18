from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime,\
    Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from ..models.users import User
import datetime


Base = declarative_base()


class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    owner_id = Column(Integer, ForeignKey(User.id))
    owner = relationship("User", back_populates="sensors")
    registries = relationship("Registry", back_populates="sensor")


class Registry(Base):
    __tablename__ = "registry"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)
    datetime = Column(DateTime, default=datetime.now())
    sensor_id = Column(Integer, ForeignKey("sensor.id"))
    sensor = relationship("Sensor", back_populates="registries")
