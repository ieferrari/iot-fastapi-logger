from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from ..db.database import Base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), index=True, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    # sensors = relationship("sensor", back_populates="owner")
