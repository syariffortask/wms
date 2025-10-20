import datetime
from enum import Enum
from sqlalchemy import table, true
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    nik: str = Field(unique=True, index=True)
    name: str = Field(nullable=False)
    password: str
    role: Role = Field(default=Role.user)
    is_active: bool = Field(default=True)
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
