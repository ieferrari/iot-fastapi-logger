from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./app_database_connection/sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "postgresql://"\
                          "webmaster:web2020blog@localhost:5432/ejemplo"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       # connect_args={"check_same_thread": False}
                       )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# for sqlite also uncomment line 11
