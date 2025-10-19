from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.item import ItemCreate, ItemRead, ItemUpdate
from app.controller.item_controller import create_item_controller
from app.controller.item_controller import get_items_controller
from app.controller.item_controller import get_item_controller
from app.controller.item_controller import update_item_controller
from app.core.database import get_session

from app.models import Item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[ItemRead])
async def read_items(session: Session =Depends(get_session)):
    return await get_items_controller(session)


@router.post("/", response_model=ItemRead)
async def create_item(data: ItemCreate, session: Session = Depends(get_session)):
    return await create_item_controller(session, data)


@router.get("/{item_id}")
async def read_item(item_id: int, session: Session = Depends(get_session)):
    return await get_item_controller(session, item_id)

@router.put("/{item_id}")
async def update_item(item_id: int, data:ItemUpdate, session: Session = Depends(get_session)):
    return await update_item_controller(session, data, item_id)
