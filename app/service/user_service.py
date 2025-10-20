from hmac import new
from sqlmodel import Session, select
from app.schemas.user import UserCreate, UserUpdate, UserLogin, UserRead
from app.core.security import hash_password, verify_password, create_access_token
from app.models import User


def register_user_service(db: Session, user: UserCreate):
    new_user  = User(
        name=user.name,
        nik=user.nik,
        role=user.role
    )
    new_user.password = hash_password(user.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_service(db: Session, id: int):
    return db.get(User, id)

def get_users_service(db: Session):
    return db.exec(select(User)).all()


def auth_user_service(session: Session, credentials: UserLogin) -> str:

    stmt = select(User).where(User.nik == credentials.nik)
    user = session.exec(stmt).first()

    if not user:
        raise ValueError("User not found")

    if not user.is_active:
        raise ValueError("User is not active")

    if not verify_password(credentials.password, user.password):
        raise ValueError("Invalid password")
    
    payload ={
    "sub": user.nik,
    "role": user.role,
    "name": user.name
    }

    return {
        "access_token": create_access_token(payload),
        "token_type": "bearer"
    }

