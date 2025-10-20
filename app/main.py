from fastapi import FastAPI
from app.api import item
from app.api import transaction

app = FastAPI()

app.include_router(item.router)
app.include_router(transaction.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
