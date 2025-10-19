from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime


if TYPE_CHECKING:
    from .transaction import Transaction  # perbaiki nama file


class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str = Field(unique=True, index=True)
    name: str = Field(nullable=False)
    stock: int = Field(default=0)
    rack: str = Field(index=True,nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = Field(default=True)
    is_deleted: bool = Field(default=False)

    transactions: List["Transaction"] = Relationship(back_populates="item")
