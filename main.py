"""Template for FastAPI applications."""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello FastAPI-template!"}
