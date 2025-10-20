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
    trx_code: str = Field(unique=True, index=True)
    trx_type: TrxType = Field(default=TrxType.IN)
    note: str = Field(nullable=True)
    created_at: datetime = Field(default_factory=datetime.now)

    # relasi
    items: List["TransactionItem"] = Relationship(back_populates="transaction")


class TransactionItem(SQLModel, table=True):
    __tablename__ = "transaction_items"

    id: Optional[int] = Field(default=None, primary_key=True)
    transaction_id: int = Field(foreign_key="transactions.id")
    item_id: int = Field(foreign_key="items.id")
    qty: int

    # relasi
    transaction: Optional["Transaction"] = Relationship(back_populates="items")
    item: Optional["Item"] = Relationship(back_populates="transaction_items")