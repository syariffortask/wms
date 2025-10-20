from annotated_types import T
from pydantic import BaseModel
from typing import Optional
from app.models import items
from app.schemas.item import ItemRead
from app.models.transaction import TrxType
from datetime import datetime
from typing import Optional, List

class TransactionItemCreate(BaseModel):
    item_id: int
    qty: int

class TransactionItemRead(BaseModel):
    id: int
    transaction_id: int
    item_id: int
    qty: int
    item: Optional[ItemRead]

class TransactionCreate(BaseModel):
    trx_type: TrxType
    note: Optional[str]
    items: list[TransactionItemCreate]

    class Config:
        from_attributes = True

class TransactionListRead(BaseModel):
    id: int
    trx_code: str
    trx_type: TrxType
    note: Optional[str]
    created_at: datetime

class TransactionDetailRead(TransactionListRead):
    items: List[TransactionItemRead]