from typing import Optional
from fastapi import HTTPException
from sqlmodel import Session
from app.service.item_service import create_item_service, get_items_service, get_item_service, update_item_service
from app.schemas.item import ItemCreate, ItemUpdate,ItemDelete
from app.models import Item


def create_item_controller(session: Session, data: ItemCreate) -> Optional[Item]:
    try:
        new_item = create_item_service(session, data)
        return new_item
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_items_controller(session: Session) -> list[Item]:
    try:
        items = get_items_service(session)
        return items
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_item_controller(session: Session, item_id: int) -> Optional[Item]:
    try:
        item = get_item_service(session, item_id)
        return item
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def update_item_controller(session: Session, data: ItemUpdate, item_id: int) -> Optional[Item]:
    try:
        item = update_item_service(session, data, item_id)
        return item
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def delete_item_controller(session: Session, item_id: int) -> Optional[Item]:
    try:
        data=ItemDelete(is_deleted=True)
        item = update_item_service(session, data, item_id)
        return item
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

