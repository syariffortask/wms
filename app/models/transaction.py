from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List,TYPE_CHECKING
from datetime import datetime
from enum import Enum

if TYPE_CHECKING:
    from .items import Item

class TrxType(str, Enum):
    IN = "in"
    OUT = "out"

class Transaction(SQLModel, table=True):
    __tablename__ = "transactions"

    id: Optional[int] = Field(default=None, primary_key=True)
    item_id: int = Field(foreign_key="items.id")
    qty: int
    trx_type: TrxType = Field(default=TrxType.IN)
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)

    item: Optional["Item"] = Relationship(back_populates="transactions")
