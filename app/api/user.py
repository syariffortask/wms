from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.schemas.user import UserCreate, UserRead, UserUpdate, UserLogin, TokenResponse
from app.controller.user_controller import login_controller
from app.controller.user_controller import register_user_controller
from app.controller.user_controller import get_users_controller
from app.controller.user_controller import get_user_controller
from app.core.database import get_session
from app.core.security import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login", response_model=TokenResponse)
async def login_user(user: UserLogin, session: Session = Depends(get_session)):
    return login_controller(user, session)

@router.post("/register", response_model=UserRead, dependencies=[Depends(get_current_user("admin"))])
def register_user(data: UserCreate, session: Session = Depends(get_session)):
    return register_user_controller(session, data)

@router.get("/users", response_model=list[UserRead], dependencies=[Depends(get_current_user("admin"))])
def read_users(session: Session = Depends(get_session)):
    return get_users_controller(session)

@router.get("/user/{user_id}", response_model=UserRead, dependencies=[Depends(get_current_user("admin"))])
def read_user(user_id: int, session: Session = Depends(get_session)):
    return get_user_controller(session, user_id)