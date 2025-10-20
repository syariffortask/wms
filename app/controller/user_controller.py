from token import OP
from fastapi import HTTPException
from sqlmodel import Session
from app.service.user_service import get_user_service, get_users_service, register_user_service, auth_user_service
from app.schemas.user import UserCreate, UserUpdate, UserLogin, UserRead, TokenResponse
from app.models import User
from typing import Optional, List

def get_user_controller(session: Session, id: int) -> Optional[User]:
    try:
        user = get_user_service(session, id)
        return user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_users_controller(session: Session) -> List[User]:
    try:
        users = get_users_service(session)
        return users
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def register_user_controller(session: Session, data: UserCreate) -> Optional[User]:
    try:
        new_user = register_user_service(session, data)
        return new_user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def login_controller(user: UserLogin, session: Session) -> TokenResponse:
    try:
        token = auth_user_service(session, user)
        return token
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    