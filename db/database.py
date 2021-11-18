from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
import os

try:
    from ..secrets import *
except ModuleNotFoundError:
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_HOST = os.environ.get('DB_HOST')

SQLALCHEMY_DATABASE_URL = "postgresql://" + \
                          DB_USER + ":" +\
                          DB_PASS + "@" + \
                          DB_HOST + ":5432/iot2"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       # connect_args={"check_same_thread": False}
                       )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
