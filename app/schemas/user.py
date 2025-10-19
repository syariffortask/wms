from pydantic import BaseModel
from typing import Optional
from app.models.user import Role


class UserRead(BaseModel):
    id: int
    username: str
    nik: str
    role: Role
    is_active: bool

    class Config:
        from_attributes = True


class UserReadSimple(BaseModel):
    id: int
    username: str
    nik: str
    role: Role

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    nik: str
    role: Role = Role.user
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    nik: Optional[str] = None
    role: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class UserLogin(BaseModel):
    nik: str
    password: str
    # beri example
    model_config = {
        "json_schema_extra": {"example": {"nik": "s0001", "password": "123"}}
    }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

