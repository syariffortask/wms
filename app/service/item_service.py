from typing import Optional
from sqlmodel import Session, select
from app.schemas.item import ItemCreate, ItemUpdate
from app.models import Item
from datetime import datetime


def get_item_service(session: Session, item_id: int) -> Optional[Item]:
    return session.get(Item, item_id)

def get_items_service(session: Session) -> list[Item]:
    return session.exec(select(Item).where(Item.is_deleted == False)).all()

def update_item_service(session: Session, data:ItemUpdate, item_id: int) -> Optional[Item]:
    try:
        item = session.get(Item, item_id)
        if item is None:
            return None
        
        # loop value dari data
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(item, key, value)
        item.updated_at = datetime.now()
        session.commit()
        session.refresh(item)
        return item
    except ValueError as ve:
        raise ve
    except Exception as e:
        session.rollback()
        raise e

def create_item_service(session: Session, data: ItemCreate) -> Optional[Item]:
    try:
        new_item = Item(
            name=data.name,
            sku=data.sku,
            rack=data.rack,
            stock=0,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            is_active=True,
            is_deleted=False
        )
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        return new_item
    
    except ValueError as ve:
        raise ve
    
    except Exception as e:
        session.rollback()
        raise e