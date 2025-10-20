from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import item
from app.api import transaction
from app.api import user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(item.router)
app.include_router(transaction.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
