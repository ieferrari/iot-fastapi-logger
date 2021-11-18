"""Template for FastAPI applications."""
from fastapi import FastAPI
from .routers import sensors, users
from .db.database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Database Conection Bbasic App",
              description="Ejemplo de conexión y manejo con base de datos"
                          "realcionales SQL",
              version="0.1.0",
              )
app.include_router(users.router)
app.include_router(sensors.router)


@app.get("/")
async def root():
    return {"msg": "Hello FastAPI-template!"}
