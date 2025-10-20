from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.item import ItemCreate, ItemRead, ItemUpdate
from app.controller.item_controller import create_item_controller
from app.controller.item_controller import get_items_controller
from app.controller.item_controller import get_item_controller
from app.controller.item_controller import update_item_controller
from app.controller.item_controller import delete_item_controller
from app.core.database import get_session
from app.core.security import get_current_user

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[ItemRead])
def read_items(session: Session =Depends(get_session)):
    return get_items_controller(session)


@router.post("/", response_model=ItemRead, dependencies=[Depends(get_current_user("admin"))])
def create_item(data: ItemCreate, session: Session = Depends(get_session)):
    return create_item_controller(session, data)


@router.get("/{item_id}", response_model=ItemRead, dependencies=[Depends(get_current_user())])
def read_item(item_id: int, session: Session = Depends(get_session)):
    return get_item_controller(session, item_id)

@router.put("/{item_id}", response_model=ItemRead, dependencies=[Depends(get_current_user("admin"))])
def update_item(item_id: int, data:ItemUpdate, session: Session = Depends(get_session)):
    return update_item_controller(session, data, item_id)

@router.delete("/{item_id}", response_model=ItemRead, dependencies=[Depends(get_current_user("admin"))])
def delete_item(item_id: int, session: Session = Depends(get_session)):
    return delete_item_controller(session, item_id)
