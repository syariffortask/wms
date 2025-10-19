from fastapi import FastAPI
from app.api import item

app = FastAPI()

app.include_router(item.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
