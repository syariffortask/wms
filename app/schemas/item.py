from unittest.mock import Base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ItemCreate(BaseModel):
    name: str
    sku: str
    rack: str

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    rack: Optional[str] = None

class ItemRead(ItemCreate):
    id: int
    stock: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ItemDelete(BaseModel):
    is_deleted: bool